import json
import os

# Only used for local solution
file_name = os.path.join("data", "accounts.json")
lesson_file_name = os.path.join("data", "lesson_data.json")
       
# Old sign up for local storage 
def old_sign_up(username, password):
    user_info = {
        "username": username,
        "password": password
    }
    
    # Read and store data
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
        
    # Update data
    data.append(user_info)
    
    # Write data
    with open(file_name, "w") as file:
        json.dump(data, file, indent=1)

# Old sign up for local storage 
def old_sign_in(username, password):
    found_user = False
    # Open database file, if dosent exist, make new file and account
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
        # Check for username and password
        for user in data:
            if user["username"] == username and user["password"] == password:
                found_user = True
        # If no username and password, sign up (change later to confirm)
        if found_user:
            print(f"Found user: {username}")
        else:
            return False
    else:
        return False
    
    return True
  
  # Update lesson progress of lesson id for local storage     

# Old Update lesson progress for local storage
def old_update_lesson_progress(username, lesson_id, lesson_result):
    found_user_data = False
    if os.path.exists(lesson_file_name):
        with open(lesson_file_name, "r") as file:
            data = json.load(file)
            for user in data:
                if user["username"] == username:
                    found_user_data = True
    else:
        data = []
        
    print(1)
        
    if not found_user_data:
        user_data = {
        "username": username,
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "" }
        data.append(user_data)
    print(2)
    for user in data:
        if user["username"] == username:
            user[f"{lesson_id}"] = lesson_result    
    
    print(3)
    with open(lesson_file_name, "w") as file:
        json.dump(data, file, indent=1)
    
# Old Get lesson progress of lesson id for local storage       
def old_get_lesson_progress(username, lesson_id):  
    if os.path.exists(lesson_file_name):
        with open(lesson_file_name, "r") as file:
            data = json.load(file)
        
        for user in data:
            if user["username"] == username:
                return user[f"{lesson_id}"]

    return f"No data found for lesson {lesson_id} for {username}!"