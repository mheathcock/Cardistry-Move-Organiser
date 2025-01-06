
import sqlite3
from pathlib import Path
from video_Storage import get_user_id

DB_PATH = Path("Cardistry.db")

"""Function to grab all videos from specific user. Will be sent to front end to display all the videos from the user"""
def grab_all_videos(username):
     #first have to grab the user_id from the passed username
     user_id = get_user_id(username)
     if user_id is None:
          print(f"ERROR: username: {username} didn't return a user_id")
          return []
     #connect to db
     db = sqlite3.connect(DB_PATH)
     cursor = db.cursor()
    #SQL command to select relevant metadata about the videos from the specific user
     cursor.execute("SELECT file_path, upload_date, notes, thumbnail_path FROM videos WHERE user_id = ?", (user_id,))
     result = cursor.fetchall()
     db.close()
     
     #turns the result of tuples into a dictionary
     video_list = [
        {"file_path": row[0], "upload_date": row[1], "notes": row[2], "thumbnail_path": row[3]} for row in result
    ]
     return video_list

"""Function to grab the video path from a specific video. Will be sent to frontend to allow the video to be played"""
def grab_video_path(video_id):
     db = sqlite3.connect(DB_PATH)
     cursor = db.cursor()
     #SQL to select the file_path from the specific video id that was passed. 
     cursor.execute("SELECT file_path FROM videos WHERE id = ?", (video_id,))
     result = cursor.fetchone()
     db.close()

     if result is None:
          print(f"ERROR: fetching video with id {video_id} failed")
          return None
     return result[0]

