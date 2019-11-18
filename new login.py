from tkinter import *
from tkinter import ttk
import os

def main_account_screen():

 global main_screen
main_screen= Tk()   # create a GUI window
main_screen.geometry("1024x800") # set the configuration of GUI window 
main_screen.title("Health Monitoring System") # set the title of GUI window


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
main_screen.geometry("1024x800")

def log_in():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("1024x800")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="User ID ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack(pady=30)
 
    Button(login_screen, text="Back", width=10, height=1, command = home_page).pack(padx=0)

   
 
def home_page():
    screen=Toplevel(main_screen)
    screen.geometry("1024x800")
    Label(screen, text="LOG IN",font="arial 15 bold").pack()
    Label(screen, text="").pack()
    b1= Button(screen, text="DOCTOR LOGIN",width=20, height=3,bd=10,command=log_in).pack(pady=50)
   
    b2=Button(screen, text="PATIENT LOGIN", width=20, height=3,bd=10,command=log_in).pack(pady=50)
 


 #  image2=image.open('C:\Users\Admin\Desktop\health.png')
  #  image1=ImageTK.PhotoImage(image2)

    

b1=Button(main_screen, text="Login", width=10, height=1, command=home_page)
b1.grid(row=0,column=6,padx=5)
    
#def main_account_screen():
 #   global main_screen

    
main_screen.mainloop()



def doctor_page():
    doctor_screen=Toplevel(main_screen)
    doctor_screen.geometry("1024x800")
    
    
    Label(doctor_screen, text="DOCTOR HOMEPAGE",font="arial 15 bold").pack()
    l2=Label(doctor_screen,text="Enter patient Id")
    l2.place(x=30,y=100)

    e=Entry()
    e.place(x=120,y=100)

    b=Button(doctor_screen,text="OK")
   
   
    Button(doctor_screen, text="Back",width=10,height=2,command=home_page).pack(pady=10)
    Button(doctor_screen, text="View all",width=20, height=3,bd=10).pack(pady=20)
def patient_page():
    patient_screen=Toplevel(main_screen)
    patient_screen.geometry("500x350")
    Label(patient_screen, text="Patient Page").pack()
    Button(patient_screen, text="view graph",width=20, height=3,bd=10).pack()
    Button(patient_screen, text="UPDATE",width=20, height=3,bd=10).pack()
   
    Button(cus_screen, text="Back",width=10,height=2,command=home_page).pack()
main_account_screen()
 
