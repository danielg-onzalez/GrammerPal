from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from database import *
from aiintegration import ask_ai_general, ask_ai_grammer
from lesson_loader import list_lessons, load_lesson
from userdata import sign_in, sign_up, update_lesson_progress

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class LoginData(BaseModel):
    username: str
    password: str

class SignupData(BaseModel):
    username: str
    password: str
    role: str

class AIRequest(BaseModel):
    username: str
    question: str

class LessonProgress(BaseModel):
    username: str
    password: str
    lesson_id: int
    result: str

# Authentication endpoints
@app.post("/login")
def login(data: LoginData):
    if sign_in(data.username, data.password):
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/signup")
def signup(data: SignupData):
    sign_up(data.username, data.password, data.role)
    return {"message": "User created successfully"}


# Lesson endpoints
@app.get("/lessons")
def get_lessons():
    return {"lessons": [file.replace(".json", "") for file in list_lessons()]}

@app.get("/lessons/{lesson_name}")
def get_lesson(lesson_name: str):
    lesson = load_lesson(lesson_name)
    if lesson:
        return {"lesson": lesson}
    raise HTTPException(status_code=404, detail="Lesson not found")

@app.post("/update-progress")
def update_progress(data: LessonProgress):
    if update_lesson_progress(data.username, data.password, data.lesson_id, data.result):
        return {"message": "Progress updated successfully"}
    raise HTTPException(status_code=400, detail="Failed to update progress")


# AI tutor endpoints
@app.post("/ask")
def ask_ai(data: AIRequest):
    connection = admin_connect_to_database()
    answer = ask_ai_general(connection, data.username, data.question)
    close_connection(connection)
    return {"answer": answer}

@app.post("/grammar-check")
def grammar_check(data: AIRequest):
    connection = admin_connect_to_database()
    answer = ask_ai_grammer(connection, data.username, data.question)
    close_connection(connection)
    return {"answer": answer}


# Test endpoint
@app.get("/test")
def test_server():
    return {"message": "FastAPI server is running successfully"}