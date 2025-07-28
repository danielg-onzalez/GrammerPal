import json
from database import *

# Sign in using database connection
def sign_in(username, password):
    connection = admin_connect_to_database()
    is_user = check_credentials(connection, username, password)
    close_connection(connection)
    if not is_user:
        return False
    return True
  
# Sign up using database connection
def sign_up(username, password, role):
    connection = admin_connect_to_database()
    add_user(connection, username, password, role, 1, "")
    close_connection(connection)   

# Update lesson progress
def update_lesson_progress(username, password, lesson_id, lesson_result):
    connection = admin_connect_to_database()
    
    if not check_credentials(connection, username, password):
        return False
    
    base_data = {
        "1": "", 
        "2": "", 
        "3": "", 
        "4": "", 
        "5": ""}

    account_data_result = get_user_data(connection, username)
    
    # If data is found load it, if not create new data
    if account_data_result:
        try:
            account_data = json.loads(account_data_result[0])
        except:
            print("Data corrupted or empty, resetting.")
            account_data = base_data
    else:
        print("No existing account data, creating new data.")
        account_data = base_data

    # Update data
    account_data[str(lesson_id)] = lesson_result  
    update_user_data(connection, username, password, account_data)
    
    close_connection(connection)
    return True

# Get lesson progress
def get_lesson_progress(username, password):
    connection = admin_connect_to_database()
    if not check_credentials(connection, username, password):
        return None
    
    account_data = get_user_data(connection, username)
    close_connection(connection)
    return account_data