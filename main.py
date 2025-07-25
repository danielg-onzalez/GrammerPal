from aiintegration import *
from userdata import *
from lesson_loader import *
from database import *

def main():
    print("Welcome to GrammarPal!\n")
    
    print_all_users()
    
    # Sign in/up
    while (True):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        
        if (sign_in(username, password)):
            print(f"Welcome back {username}!")
            break
        else:
            signup_choice = input("We didn't find your account, would you like to try again [1] or signup[2]?")
            role = input("Are you a \"student\", \"teacher\", or \"parent\"?");
            match signup_choice:
                case "1": continue
                case "2": 
                    sign_up(username, password, role)
                    break

    # Select Lessons
    connection = admin_connect_to_database()
    while (True):
        lessons = list_lessons()

        for lesson_id, file in enumerate(lessons):
            print(f"{lesson_id + 1}. {file.replace('.json', '')}")
    
        lesson_choice = input("\nEnter the number of the lesson you'd like to start: ")

        #try:
        lesson_id = int(lesson_choice) - 1
        lesson_name = lessons[lesson_id].replace(".json", "")
        lesson = load_lesson(lesson_name)
        if lesson:
            update_lesson_progress(username, password, int(lesson_choice), display_lesson(connection, username, lesson))
        #except:
            #print("Invalid choice, please try again.")
        
        continue_choice = input("Would you like to do another lesson? Yes [1], No [2].")
        match continue_choice:
            case "1": continue
            case "2": break
            
    print("Thanks for using GrammarPal! We hope to see you again!")
    close_connection(connection)
    
main()

def update():
    connection = admin_connect_to_database()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM accounts WHERE username = 'ash'")
    connection.close()
    
#update()