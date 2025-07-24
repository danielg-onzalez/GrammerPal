from google import genai
from parental_controls import *

client = genai.Client(api_key="AIzaSyAA7PyrLZd_S06RoTzRdbd_OBmwUArCk4M")

rules = "Rules for response: Keep response short, be precise and and friendly, discourage bad words or profanity, be positive but maintain teacher like criticism when needed, and finally stay on task with the response and try not to deviate from teaching the student."

# Ask Question to AI
ask_prompt = "You are a tutor for elemenatary school students. Please provide an engaging and child freindly response to the following question:"
def ask_ai_general(username, user_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"{rules} {ask_prompt} Your students name is {username}. {get_parental_control_level(username)} {user_prompt}"
    )
    return response.text

# Get Grammer Advice from AI
grammer_prompt = "You are a tutor for elemenatary school students. Please provide grammar advice for the following sentence:"
def ask_ai_grammer(username, user_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"{rules} {grammer_prompt} Your students name is {username}. {get_parental_control_level(username)} {user_prompt}"
    )
    return response.text