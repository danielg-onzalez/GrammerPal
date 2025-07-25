import json
import os
from aiintegration import *
from userdata import *

lesson_file_name = "lessons"

def list_lessons():
    return [file for file in os.listdir(lesson_file_name) if file.endswith(".json")]

def load_lesson(lesson_name):
    try:
        file_path = os.path.join(lesson_file_name, lesson_name + ".json")
        with open(file_path, "r") as file:
            return json.load(file)
    except:
        print("Lesson not found.")
        return None

def display_lesson(username, lesson):
    print(f"\nLesson: {lesson['title']}")
    print(f"Objective: {lesson['objective']}")
    print(f"Estimated Time: {lesson['estimatedDurationMinutes']} minutes\n")

    for section in lesson["lessonFlow"]:
        print(f"\n--- {section['type'].capitalize()} ---")

        # Introduction
        if section["type"] == "introduction":
            print(section["content"])

        # Rule Explination 
        elif section["type"] == "explination":
            for rule in section["rules"]:
                print(f"Rule: {rule['rule']}")
                print(f"Example: {rule['example']}")

        # Practice
        elif section["type"] == "practice":
            for act in section["activities"]:
                while True:
                    
                    # Check practice type, if correct, escape loop
                    if act["activityType"] == "multipleChoice":
                        print(f"\n{act['question']}")
                        for i, opt in enumerate(act["options"]):
                            print(f"  {chr(65+i)}. {opt}")
                        choice = input("Your answer (A/B/C...): ")
                        if choice == act['answer']:
                            break
                    elif act["activityType"] == "fillInTheBlank":
                        print(f"\nComplete: {act['sentence']}")
                        choice = input("Your answer: ")
                        if choice == act['answer']:
                            break
                        
                    # If not right awnser, explain
                    print(f"{act['explination']}")
                    
                # Print right answer and go on to next
                print(act['rightAnswer'])
                
        # Quiz
        elif section["type"] == "quiz":
            
            # Check for questions, if correct, escape loop
            for q in section["questions"]:
                while True:
                    print(f"\nQuiz: {q['question']}")
                    choice = input("Your answer: ")
                    if choice == q['answer']:
                        break
                    
                    # If wrong print explination
                    print(q['explination'])  
                
                # Print right answer and go on to next
                print(act['rightAnswer'])  

        # AI Feedback
        elif section["type"] == "aiPrompt":
            print(f"\nAI Prompt: {section['instruction']}")
            student_input = input("Your response: ")
            print("Asking the AI for feedback...")
            feedback =  "fake awnser haiiii xD :3" #ask_ai_grammer(username, student_input) Limits sucks huh :/
            print(f"AI Feedback:\n{feedback}")

        # Print lesson end feedback
        elif section["type"] == "feedback":
            print(f"\n{section['message']}")

    # Print results
    lesson_result = f"{lesson['rewards']['points']} points" 
    print(f"\nYou earned: {lesson['rewards']['badge']} (+{lesson_result})")
    #print(f"Next Lesson: {lesson['nextLessonId']}")
    return lesson_result
