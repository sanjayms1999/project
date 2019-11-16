from tkinter import *
from tkinter import ttk
import os
def main_account_screen():
    global main_screen
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("Health Monitoring System") # set the title of GUI window
    
    
    main_screen.geometry("300x250")

    
    Label(main_screen, text="Please enter details below to login").pack()
    Label(main_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()
    Label(main_screen, text="Username  ").pack()
    username_login_entry = Entry(main_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="Password  ").pack()
    password__login_entry = Entry(main_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Login", width=10, height=1, command=home_page).pack()
    main_screen.mainloop()
def home_page():
    screen=Toplevel(main_screen)
    screen.geometry("300x250")
    Label(screen, text="Home Page").pack()
    Label(screen, text="").pack()
    Button(screen, text="DOCTOR LOGIN",width=20, height=3,bd=10,command=log_in).pack()
    Button(screen, text="PATIENT LOGIN", width=20, height=3,bd=10,command=log_in).pack()
   
def log_in():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
  

def log_in():
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 

 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username  ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password  ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 



########
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()

def doctor_page():
    doctor_screen=Toplevel(main_screen)
    doctor_screen.geometry("500x350")
    Button(doctor_screen, text="view all patients").pack()
    Button(doctor_screen, text="patient1",width=20, height=3,bd=10).pack()
    Button(doctor_screen, text="patient2",width=20, height=3,bd=10).pack()
    Button(doctor_screen, text="patient3",width=20, height=3,bd=10).pack()
    Button(doctor_screen, text="BP Graph",width=20, height=3,bd=10).pack()
    Button(doctor_screen, text="Temp Graph",width=20, height=3,bd=10).pack()
    Button(doctor_screen, text="Search",width=20, height=3,bd=10).pack()
   
    Button(doctor_screen, text="Back",width=10,height=2,command=log_in).pack()
def patient_page():
    patient_screen=Toplevel(main_screen)
    patient_screen.geometry("500x350")
    Label(patient_screen, text="Patient Page").pack()
    Button(patient_screen, text="view graph",width=20, height=3,bd=10).pack()
    Button(patient_screen, text="UPDATE",width=20, height=3,bd=10).pack()
   
    Button(cus_screen, text="Back",width=10,height=2,command=log_in).pack()
main_account_screen()
 
