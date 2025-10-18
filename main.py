from tkinter import *
from tkinter import messagebox 
from backend.auth import login_User, register_User
import customtkinter as CTk
from backend.video_Retrieval import *
from PIL import Image, ImageTk
import os

app = CTk.CTk()
app.geometry("1920x1080")
app.configure(bg="#121212")
app.state('zoomed')  

"""
Front end GUI for user authentication.
"""
def login_or_register_gui():
    #forget previous widgets
    for widget in app.winfo_children():
        widget.destroy()
    
  
    app_frame = CTk.CTkFrame(app, fg_color="transparent")
    app_frame.pack(expand=True,anchor="center")

    app.title("Login / Register")
    
   
    CTk.CTkButton(
        app_frame, 
        text="Login", 
        command=login_gui, 
        width=250, 
        height=50, 
        font=CTk.CTkFont(family="Helvetica Neue LT Std",size=30, weight="bold"),
        corner_radius=30,
        fg_color="#BB86FB", 
        hover_color="#9C5AF7"
    ).pack(pady=10)
    
    CTk.CTkButton(
        app_frame, 
        text="Register", 
        command=register_gui, 
        width=250, 
        height=50, 
        font=CTk.CTkFont(family="Helvetica Neue LT Std",size=30, weight="bold"),
        corner_radius=30,
        fg_color="#BB86FB", 
        hover_color="#9C5AF7"
    ).pack(pady=10) 

def login_gui():
       #forget previous widgets
    for widget in app.winfo_children():
        widget.destroy()
    
    app.title("Login")
    
    CTk.CTkButton(
        app, 
        text="Back", 
        width=100, 
        height=30, 
        command=login_or_register_gui,
        fg_color="gray", 
        hover_color="darkgray"
    ).pack(side="top", anchor="nw", pady=10, padx=10)#Back button to return to login/register choice screen
    main_Frame = CTk.CTkFrame(
        master=app,
        fg_color="#BB86FB",
        corner_radius=150,
        border_width=0
    )
    main_Frame.pack(expand=True, fill='x', anchor="center", padx=500)

    login_frame = CTk.CTkFrame(
        master = main_Frame,
        fg_color="transparent"
        ) 
    # Center the frame in the window
    login_frame.pack(expand=True, fill="both", padx=50, pady=50)
    

    # Page Title
    CTk.CTkLabel(
        master=login_frame, 
        text="LOGIN", 
        font=CTk.CTkFont(family="Summer Dream Sans Demo", size=60, weight="bold"),
        text_color="white"
    ).pack(pady=(40, 40))

    #Create two labels, Username and Password, two entry fields for input 
    username_entry = CTk.CTkEntry(
    master=login_frame,
    placeholder_text="Username",
    font=CTk.CTkFont(family="Helvetica Neue LT Std",size=30, weight="normal"),
    width=450,
    height=60,
    corner_radius=30, 
    fg_color="white",
    text_color="#171717",
    border_width=0
    )
    username_entry.pack(pady=(20, 10), padx=50)

    password_entry = CTk.CTkEntry(
    master=login_frame,
    placeholder_text="Password",
    font=CTk.CTkFont(family="Helvetica Neue LT Std",size=30, weight="normal"),
    show="*", # Hides the text as dots for a password field
     width=450,
    height=60,
    corner_radius=30, 
    fg_color="white",
    text_color="#171717",
    border_width=0
    )
    password_entry.pack(pady=60, padx=50)


#PRINT STATEMENTS FOR DEBUGGING
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}, Password: {password}")

    #Function to handle login result
    def login_result():
        if login_User(username_entry.get(), password_entry.get()):
            print("Login successful")
            display_video_gui(username_entry.get())
        else:
            print("Login failed")
            messagebox.askretrycancel("Login Fail", "Username or Password Incorrect. Try again?") 
            username_entry.delete(0, END)
            password_entry.delete(0, END)   

    #Login button that calls the login_result function when clicked
    CTk.CTkButton(
        login_frame, 
        text="SUBMIT",
        font=CTk.CTkFont(family="Helvetica Neue LT Std",size=40, weight="bold"),
        text_color="white",
        width=200, 
        height=50, 
        corner_radius=35,
        fg_color="black", 
        hover_color="#333333",
        command=login_result
    ).pack(pady=(20, 5))
  


def register_gui():
          #forget previous widgets
    for widget in app.winfo_children():
        widget.destroy()
    app.title("Register")

    #Back button to return to login/register choice screen
    CTk.CTkButton(
        app, 
        text="Back", 
        width=100, 
        height=30, 
        command=login_or_register_gui,
        fg_color="gray", 
        hover_color="darkgray"
    ).pack(side="top", anchor="nw", pady=10, padx=10)
    main_Frame = CTk.CTkFrame(
        master=app,
        fg_color="#BB86FB",
        corner_radius=150,
        border_width=0
    )
    main_Frame.pack(expand=True, fill='x', anchor="center", padx=500)

    register_frame = CTk.CTkFrame(
        master = main_Frame,
        fg_color="transparent"
        ) 
    #center the frame in the window
    register_frame.pack(expand=True, fill="both", padx=50, pady=50)
    

    #page Title
    CTk.CTkLabel(
        master=register_frame, 
        text="REGISTER", 
        font=CTk.CTkFont(family="Summer Dream Sans Demo", size=60, weight="bold"),
        text_color="white"
    ).pack(pady=(40, 40))

    #create two labels, Username and Password, two entry fields for input 
    username_entry = CTk.CTkEntry(
    master=register_frame,
    placeholder_text="Username",
    font=CTk.CTkFont(family="Helvetica Neue LT Std",size=30, weight="normal"),
    width=450,
    height=60,
    corner_radius=30, 
    fg_color="white",
    text_color="#171717",
    border_width=0
    )
    username_entry.pack(pady=(20, 10), padx=50)


    password_entry = CTk.CTkEntry(
    master=register_frame,
    placeholder_text="Password",
    font=CTk.CTkFont(family="Helvetica Neue LT Std",size=30, weight="normal"),
    show="*", #hides the text as dots for a password field
     width=450,
    height=60,
    corner_radius=30, 
    fg_color="white",
    text_color="#171717",
    border_width=0
    )
    password_entry.pack(pady=60, padx=50)


#PRINT STATEMENTS FOR DEBUGGING
    username = username_entry.get()
    password = password_entry.get()
    print(f"Register Username: {username}, Register Password: {password}")

  #Function to handle registration result
    def register_result():
        if register_User(username_entry.get(), password_entry.get()):
            print("Registration successful")
            messagebox.showinfo("Registration Success", "User registered successfully. Please login.")
            login_gui(username)
        else:
            print("Registration failed")
            messagebox.showerror("Registration Fail", "Username already exists. Try a different one.") 
            username_entry.delete(0, END)
            password_entry.delete(0, END)  

    #Login button that calls the login_result function when clicked
    CTk.CTkButton(
        register_frame, 
        text="SUBMIT",
        font=CTk.CTkFont(family="Helvetica Neue LT Std",size=40, weight="bold"),
        text_color="white",
        width=200, 
        height=50, 
        corner_radius=35,
        fg_color="black", 
        hover_color="#333333",
        command=register_result
    ).pack(pady=(20, 5))
  

def show_video_player_gui(username, video_path):
    for widget in app.winfo_children():
        widget.destroy()
    app.title("Video Player")
    #Back button to return to video gallery
    CTk.CTkButton(
        app, 
        text="Back", 
        width=100, 
        height=30, 
        command=lambda: display_video_gui(username),
        fg_color="gray", 
        hover_color="darkgray"
    ).pack(side="top", anchor="nw", pady=10, padx=10)

    video_frame = CTk.CTkFrame(
        app,
        fg_color="#121212",
        corner_radius=35
    )
    video_frame.pack(expand=True, fill="both", padx=100, pady=100)
    


"""
Front end GUI for displaying videos and their thumbnails.
"""

def display_video_gui(username):
    #forget previous widgets
    for widget in app.winfo_children():
        widget.destroy() 
    app.title(f"Video Gallery - {username}") #Title includes the logged in username
    #Main content frame to hold video thumbnails
    main_content_frame = CTk.CTkFrame(
        app, 
        fg_color="#121212",
        corner_radius=30
    
    )
    main_content_frame.pack(fill="both", expand=True)

    #Fetch all videos for the logged in user
    user_videos = grab_all_videos(username)

    #Main logic to display video thumbnails in a grid
    if user_videos:#If there are videos for the user
        CTk.CTkLabel(main_content_frame, text="Your Uploaded Videos", font=CTk.CTkFont(size=30, weight="bold")).pack(pady=(20, 10))
        thumbnail_grid_frame = CTk.CTkFrame(main_content_frame, fg_color="transparent")
        thumbnail_grid_frame.pack(pady=10, padx=20, anchor="n")

        MAX_COLUMNS = 4 #how many items can be in a single row

        #Iterate through all videos and place them in the grid
        for index, video in enumerate(user_videos):
            video_path = video.get("video_path") # Extract the video path needed for playback
            thumbnail_path = video.get("thumbnail_path")
            notes = video.get('notes', 'No Notes Provided')
            #These two calculations will decide where in the grid each video thumbnail will go. It basically goes up until the max_columns is reached then starts a new row.
            row = index // MAX_COLUMNS #// returns largest whole number of times the divisor fits into the divident. Eg index 0-3 /4 will equal 0 hence first row index 4-7 /4 will equal 1 hence second row etc
            column = index % MAX_COLUMNS #similar to row but % returns the remainder of the division. Eg index 0-3 %4 will equal 0-3 going up the columns until 4%4 which will reset to 0 starting the new row in the first column again.

            video_card = CTk.CTkFrame(thumbnail_grid_frame, fg_color="#BB86FB", corner_radius=35, width=220, height=250)
            video_card.grid(row=row, column=column, padx=15, pady=15, sticky="nsew")#.grid places the frame in the grid at the calculated row and column with padding around each card
            if thumbnail_path:
                try:
                    #Try open the Image using PIL
                    thumbnail_image = Image.open(thumbnail_path)
                    #Create the CTkImage object resized to fit the card
                    ctk_image = CTk.CTkImage(light_image=thumbnail_image, dark_image=thumbnail_image, size=(200, 150))
                    
                    #Makes a button with the thumbnail image that opens the video player when clicked
                    image_button = CTk.CTkButton(
                        video_card, 
                        text="", 
                        image=ctk_image,
                        command=lambda path=video_path: show_video_player_gui(username, path), # Command to open the video
                        fg_color="transparent",
                        hover_color="#9C5AF7", 
                        width=200,
                        height=150,
                        border_width=0,
                        cursor="hand2"
                    )
                    image_button.pack(pady=(10, 5), padx=10)
                    
                    #Keep a persistent reference to the image object to prevent garbage collection
                    image_button.image_ref = ctk_image
                    
                    #Create a CTkLabel for the notes below the image
                    notes_label = CTk.CTkLabel(video_card, text=notes, width=200, wraplength=200, compound="center", font=CTk.CTkFont(size=14), text_color="white")
                    notes_label.pack(pady=(0, 10), padx=10)

                except FileNotFoundError:#Handles case where thumbnail file is missing. Thumbnail path exists in db but file not found on disk
                    CTk.CTkLabel(video_card, text="Thumbnail not found.", text_color="#FF4500").pack(pady=5)
                    CTk.CTkLabel(video_card, text=notes, wraplength=180).pack(pady=5)#notes still displayed
                except Exception as e: #Handles any other exceptions that may occur
                    CTk.CTkLabel(video_card, text=f"Error loading image.", text_color="#FF4500").pack(pady=5)
                    CTk.CTkLabel(video_card, text=f"Details: {e}", wraplength=180).pack(pady=5)#error details displayed
                
            else:#Handles the case where thumbnail_path is None. No thumbnail was generated for the video
                # Placeholder button when no thumbnail exists
                no_thumb_button = CTk.CTkButton(
                    video_card, 
                    text="No Thumbnail\n(Click to Play)", 
                    font=CTk.CTkFont(size=18, weight="bold"),
                    command=lambda path=video_path: show_video_player_gui(username, path),
                    width=200, 
                    height=150,
                    fg_color="#404040", 
                    hover_color="#505050",
                    cursor="hand2"
                )
                no_thumb_button.pack(pady=(10, 5), padx=10)
                
                CTk.CTkLabel(video_card, text=notes, wraplength=180).pack(pady=5)#notes still displayed
            
    else: #Handles the case where user_videos is empty (User has no videos to show)
        CTk.CTkLabel(main_content_frame, text="No videos found.", font=CTk.CTkFont(size=24, weight="bold")).pack(pady=20)

    
login_or_register_gui()
app.mainloop()