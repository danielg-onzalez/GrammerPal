from getpass import getpass
from mysql.connector import connect, Error
import json

def admin_connect_to_database():
    db_user = "admin"
    db_pass = "7956"
    return connect_to_database(db_user, db_pass)

# Connect to database using username and password
def connect_to_database(database_username, database_password):
    try:
        connection = connect(
            host = "47.198.199.19",
            user = database_username,
            password = database_password,
            database = "grammarpal_account_info"
        )
    except Error as e:
        print(e)
    
    if connection:
        return connection
    else:
        return None
   
# !! Close database connection
def close_connection(connection):
    cursor = connection.cursor()
    cursor.close()
    connection.close()
       
# Add a new user and account data
def add_user(connection, username, password, account_data):
    cursor = connection.cursor()
    
    sql = "INSERT INTO accounts (username, password, account_data) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql, (username, password, account_data,))
        connection.commit()
        print("User added successfully.")
    except connect.Error as err:
        print("Error:", err)

# Check is username and password match
def check_credentials(connection, username, password):
    cursor = connection.cursor()
    
    sql = "SELECT password FROM accounts WHERE username = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    
    try:
        if result[0] == password:
            return True
        else:
            return False
    except:
        return False
    
# Retrieve user data
def get_user_data(connection, username):
    cursor = connection.cursor()
    
    sql = "SELECT account_data FROM accounts WHERE username = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    if not result:
        return None
    return result

# Update user data
def update_user_data(connection, username, password, new_account_data):
    cursor = connection.cursor()
    
    # Check credentials
    if not check_credentials(connection, username, password):
        return None
    
    # Update data
    new_data = json.dumps(new_account_data)
    sql = "UPDATE accounts SET account_data = %s WHERE username = %s"
    cursor.execute(sql, (new_data, username))
    connection.commit()
    print(f"Updated data for {username}.")
    
# Print all users and data for testing purposes
def print_all_users():
    connection = connect_to_database("admin", "7956")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts")
    results = cursor.fetchall()

    print("All users in database:")
    for row in results:
        id, username, password, account_data = row
        
        # Check if data is empty or null
        if account_data:
            try:
                account_data_result = json.loads(account_data)
            except json.JSONDecodeError:
                account_data_result = "Invalid JSON."
        else:
            account_data_result = "No data found."

        print(f"ID: {id} | Username: {username} | Password: {password} | Account Data: {account_data_result}")
    
    close_connection(connection)