import sqlite3
import bcrypt
from pathlib import Path
import db

DB_PATH = Path("db.sqlite")



def register_User(username, password):
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()

    #Hash password before trying to add to DB.
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        #Insert new USER into db
        cursor.execute("""
                       INSERT INTO users (username, password)
                       VALUES(?, ?);
                       """, (username, hashed_password))
        db.commit()
        print("USER added to db")
        return True
    #Catch a repeated username
    except sqlite3.IntegrityError:
        print("ERROR: USERNAME exists.")
        return False
    finally:
        db.close()

def login_User(username, password):
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    #Select the hashed pw of the user with matching username 
    cursor.execute("""SELECT password FROM users WHERE username = ?;
                   """, (username,))
    result = cursor.fetchone() #single row column because were selecting one column not multiple so element will be index 0 
    db.close()

    if result:
        hashed_password = result[0]
        
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password): #checks hashed password entry matches the db hashed password
            print("Login successful")
            return True
    print("ERROR: Invalid username or password")
    return False

#test cases
"""
if __name__ == "__main__":
    print("1. Registering a new user...")
    register_User("test_user", "secure_password")

    print("2. Logging in...")
    login_User("test_user", "secure_password")  # Should succeed
    login_User("test_user", "wrong_password")  # Should fail
"""