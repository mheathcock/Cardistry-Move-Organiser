from tkinter import *
from tkinter import messagebox 
from backend.auth import login_User, register_User
import customtkinter as CTk



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
            upload_video_gui()
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
            login_gui()
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
  




"""
Front end GUI for uploading videos and storing metadata.
"""
def upload_video_gui():
          #forget previous widgets
    for widget in app.winfo_children():
        widget.destroy() 
    app.title("Upload Video")


    Label(app, text="Upload Video", font=("Arial", 24)).pack(pady=20)


   
    
login_or_register_gui()
app.mainloop()