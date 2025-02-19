import sqlite3
from pathlib import Path

DB_PATH = Path("Cardistry.db")

def init_db():
  #Connect to db / create if it doesn't exist
  db = sqlite3.connect(DB_PATH)

#cursor obj to execute SQL 
  cursor = db.cursor()

  #user table for login, username and id unique  
  cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 username TEXT UNIQUE NOT NULL, 
                 password TEXT NOT NULL
                 );
                 """)
  #video table for upload
  cursor.execute("""CREATE TABLE IF NOT EXISTS videos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER NOT NULL,
                   file_path TEXT NOT NULL,
                   upload_date TEXT NOT NULL,
                   tags TEXT,
                   notes TEXT,
                   thumbnail_path TEXT NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users(id)
                   );
                   """)






  #commit changes
  db.commit()
 #close connection when done 
  db.close()
def check_table_schema():
    db = sqlite3.connect("Cardistry.db")
    cursor = db.cursor()
    cursor.execute("PRAGMA table_info(videos);")
    columns = cursor.fetchall()
    db.close()
    print(columns)  # This will print out all the columns in the "videos" table

if __name__ == "__main__":
    init_db()
    print("Database initialized!")

check_table_schema()