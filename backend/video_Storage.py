import os 
import shutil
import time
from tkinter import filedialog
import sqlite3
from datetime import datetime 
from pathlib import Path
import subprocess


DB_PATH = Path("Cardistry.db")
"""Getter function for grabbing the associated id from username"""
def get_user_id(username):
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    #SQL Select the id associated with the username
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))#pass username inside a tuple to avoid incorrect number of bindings error
    result = cursor.fetchone()
    db.close()
    if result:
        return result[0]
    else:
        print(f"ERROR: User '{username}' not found")
        return None

"""Function to check if the user's folder exists and creates the folder if not. Users videos will be stored in said folder """
def create_user_folder(username):

    #user_folder is defined as the folder path "uploads/{username}"
    user_folder = os.path.join("uploads", username)

    print(f"Creating user folder: '{user_folder}'")

    #if folder doesn't exist make it
    if not os.path.exists(user_folder):
        try:
            os.makedirs(user_folder)
            print(f"Folder created: '{user_folder}'")
        except Exception as e:
            print(f"Error creating folder: {e}")
            return None
    return user_folder

"""Function to upload a video to the user's unique folder"""
def upload_video(username):
    #filedialog.askopenfilename lets the user choose a video file to upload
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")])

    print(f"Selected file path: {file_path}")

    if file_path:
       # return user folder or create the user folder if doesn't exist
       user_folder = create_user_folder(username)

       print(f"User folder path: {user_folder}")
      #Generate filename using timestamp + original filename
       new_filename = os.path.join(user_folder, f"{int(time.time())}_{os.path.basename(file_path)}")
       print(f"New filename: {new_filename}")
    # Copy video file to the user's folder
       shutil.copy(file_path, new_filename)

       print(f"Video uploaded and saved as: {new_filename}")
       return new_filename #return path to uploaded video
    else:
        print("ERROR: no file selected")
        return None
    
"""Function to update the database with the users new video """
def insert_video_to_db(user_id, video_path, notes, thumbnail_path):
     db = sqlite3.connect(DB_PATH)
     cursor = db.cursor()
    #SQL to insert relevant video metadata to the db
     cursor.execute("""
                    INSERT INTO videos (user_id, file_path, upload_date, notes, thumbnail_path) 
                    VALUES(?, ?, ?, ?, ?);
                    """,(user_id, video_path, datetime.now(), notes, thumbnail_path))
     
     video_id = cursor.lastrowid
     db.commit()
     db.close()
     print(f"video data saved: {video_path}")
     return video_id

"""Wrapper to the upload_video function and insert the metadata into the db as well."""
def upload_and_store_video(username):
    user_id = get_user_id(username)
    video_path = upload_video(username)

    #if upload successful ask the user if they have any notes on the move to be stored alongside
    if video_path:
        notes = input("Any notes on the move?: ")

        video_id = insert_video_to_db(user_id, video_path, notes, "")

        thumbnail_path = os.path.join(os.path.dirname(video_path), f"{video_id}_thumbnail.jpg")

        generate_thumbnail(video_path, thumbnail_path)

        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()
        cursor.execute("UPDATE videos SET thumbnail_path = ? WHERE id = ?", (thumbnail_path, video_id))
        db.commit()
        db.close()

        print(f"Video {video_path} uploaded and saved")
    else:
        print("ERROR: video upload failed")

def generate_thumbnail(video_path, thumbnail_path):
     try:
        # Run the FFmpeg command to create a thumbnail
        subprocess.run([
            'ffmpeg', '-i', video_path,  # Input video
            '-ss', '00:00:01.000',  # Timestamp to capture the thumbnail from (1 second in)
            '-vframes', '1',  # Capture only 1 frame
            thumbnail_path  # Output path for the thumbnail
        ], check=True)
        print(f"Thumbnail generated at {thumbnail_path}")
     except subprocess.CalledProcessError as e:
         print(f"ERROR generating thumbnail: {e}")


#Test case

if __name__ == "__main__":
        upload_and_store_video("test_user2")
       