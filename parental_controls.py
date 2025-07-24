import json
import os

parental_control_file_name = "parental_controls.json"

# AI prompt control levels
level_1 = "The parent of this student requests you keep the prompt kid friendly."
level_2 = "The parent of this student requests you keep the prompt kid very friendly and make sure to double check not to use any innapropriate language."
level_3 = "The parent of this student requests you keep the prompt VERY kid friendly. Do not use any uncessary wording that could even possible be considered innapropriate. You must be professional as if you were a dedicated teacher."

# high key you could erase another users settings but like i dun wanna deal with it

# Sets the parental control level for a user
def set_parental_control_level(username, level):
    # Set levels min/max
    if level > 3:
        level = 3
    elif level < 1:
        level = 1
    
    control_info = {
        "username": username,
        "parental_control_level": level
    }
    found_controls = False
    
    if os.path.exists(parental_control_file_name):
        with open(parental_control_file_name, "r") as file:
            try:
                data = json.load(file)
                for user in data:
                    if user["username"] == username:
                        user["parental_control_level"] = level
                        found_controls = True
            except json.JSONDecodeError:
                data = []
                    
            if not found_controls:
                data = []
                data.append(control_info)
                
        with open(parental_control_file_name, "w") as file: 
            json.dump(data, file, indent=1)

# Gets the parental control level for a user
def get_parental_control_level(username):
    if os.path.exists(parental_control_file_name):
        with open(parental_control_file_name, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return f"No parental controls set for {username}!"
        
        for user in data:
            if user["username"] == username:
                return user["parental_control_level"]

# Gets the AI prompt for the parental control level
def get_parental_control_prompt_settings(username):
    level = get_parental_control_level(username)
    match level:
        case 1: 
            return level_1
        case 2:
            return level_2
        case 3:
            return level_3
            