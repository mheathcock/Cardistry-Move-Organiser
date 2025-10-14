from tkinter import *
from tkinter import messagebox 
from backend.auth import login_User, register_User



app = Tk()
app.geometry("1920x1080")

"""
Front end GUI for user authentication.
"""
def login_or_register_gui():
    #forget previous widgets
    for widget in app.winfo_children():
        widget.destroy()
    app_frame = Frame(app)
    app_frame.pack(expand=True,anchor="center")

    app.title("Login / Register")
    button = Button(app_frame, text="Login", command=login_gui, width=20, height=2)
    button.pack(pady=10)
    button = Button(app_frame, text="Register", command=register_gui, width=20, height=2)
    button.pack(pady=10)    

def login_gui():
       #forget previous widgets
    for widget in app.winfo_children():
        widget.destroy()
    
    app.title("Login")
    Button(app, text="Back", width=20, height=2, command=login_or_register_gui).pack(side="top", anchor="nw", pady=10, padx=10)#Back button to return to login/register choice screen
    Label(app, text="Login", font=("Arial", 30)).pack() # Page Title
    login_frame = Frame(app) # Frame to hold login form elements
    login_frame.pack(expand=True,anchor="center") # Center the frame in the window


    #Create two labels, Username and Password, two entry fields for input 
    Label(login_frame, text="Username", font=("Arial", 14)).pack(pady=10)
    e1 = Entry(login_frame,width=30)
    e1.pack(pady=5)

    Label(login_frame, text="Password", font=("Arial", 14)).pack(pady=10)
    e2 = Entry(login_frame, width=30, show="*")
    e2.pack(pady=5)


#PRINT STATEMENTS FOR DEBUGGING
    username = e1.get()
    password = e2.get()
    print(f"Username: {username}, Password: {password}")

    #Function to handle login result
    def login_result():
        if login_User(e1.get(), e2.get()):
            print("Login successful")
            upload_video_gui()
        else:
            print("Login failed")
            messagebox.askretrycancel("Login Fail", "Username or Password Incorrect. Try again?") 
            e1.delete(0, END)
            e2.delete(0, END)   

    #Login button that calls the login_result function when clicked
    Button(login_frame, text="Login", 
           width=20, height=2, 
           command=lambda: login_result()
           ).pack(pady=20)
  


def register_gui():
          #forget previous widgets
    for widget in app.winfo_children():
        widget.destroy()
    app.title("Register")

    Button(app, text="Back", width=20, height=2, command=login_or_register_gui).pack(side="top", anchor="nw", pady=10, padx=10) #Back button to return to login/register choice screen
    Label(app, text="Register", font=("Arial", 30)).pack()# Page Title

    #Frame to hold register form elements
    register_frame = Frame(app)
    register_frame.pack(expand=True,anchor="center")


    #Create two labels, Username and Password, two entry fields for user input
    Label(register_frame, text="Username", font=("Arial", 14)).pack(pady=10)
    e1 = Entry(register_frame,width=30)
    e1.pack(pady=5)

    Label(register_frame, text="Password", font=("Arial", 14)).pack(pady=10)
    e2 = Entry(register_frame, width=30, show="*")
    e2.pack(pady=5)

##PRINT STATEMENTS FOR DEBUGGING
    username = e1.get()
    password = e2.get()
    print(f"Register Username: {username}, Register Password: {password}")

#Function to handle registration result
    def register_result():
        if register_User(e1.get(), e2.get()):
            print("Registration successful")
            messagebox.showinfo("Registration Success", "User registered successfully. Please login.")
            login_gui()
        else:
            print("Registration failed")
            messagebox.showerror("Registration Fail", "Username already exists. Try a different one.") 
            e1.delete(0, END)
            e2.delete(0, END)
    #Register button that calls the register_result function when clicked
    Button(register_frame, text="Login", 
           width=20, height=2, 
           command=lambda: register_result()
           ).pack(pady=20)
    





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