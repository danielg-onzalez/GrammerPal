from google import genai
from database import *

# Google API connection (NOT SAFE!!!)
client = genai.Client(api_key="AIzaSyAA7PyrLZd_S06RoTzRdbd_OBmwUArCk4M")

# Rules for AI
rules = "Rules for response: Keep response short, be precise and and friendly, discourage bad words or profanity, be positive but maintain teacher like criticism when needed, and finally stay on task with the response and try not to deviate from teaching the student."

# Ask Question to AI
ask_prompt = "You are a tutor for elemenatary school students. Please provide an engaging and child freindly response to the following question:"
def ask_ai_general(connection, username, user_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"{rules} {ask_prompt} Your students name is {username}. {get_parental_control_prompt_settings(connection, username)} {user_prompt}"
    )
    return response.text

# Get Grammer Advice from AI
grammer_prompt = "You are a tutor for elemenatary school students. Please provide grammar advice for the following sentence:"
def ask_ai_grammer(connection, username, user_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"{rules} {grammer_prompt} Your students name is {username}. {get_parental_control_prompt_settings(connection, username)} {user_prompt}"
    )
    return response.text

# AI prompt control levels
level_1 = "The parent of this student requests you keep the prompt kid friendly."
level_2 = "The parent of this student requests you keep the prompt kid very friendly and make sure to double check not to use any innapropriate language."
level_3 = "The parent of this student requests you keep the prompt VERY kid friendly. Do not use any uncessary wording that could even possible be considered innapropriate. You must be professional as if you were a dedicated teacher."

# Gets the AI prompt for the parental control level
def get_parental_control_prompt_settings(connection, username):
    level = get_user_parental_control_level(connection, username)
    match level:
        case 1: 
            return level_1
        case 2:
            return level_2
        case 3:
            return level_3