from tkinter import *
import os
 
# Designing window for registration
 
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(login_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("1024x800")

    #c=Canvas(login_screen,width=1024,height=800,bg="white")
    #c.pack()
    #photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bgss.png')
    #background_label=Label(login_screen,image=photo)
    #background_label.place(x=0,y=0)
    
    
   
    Label(login_screen, text="Please enter details below to login").place(x=450,y=0)
    #Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username  ").place(x=250,y=200)
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.place(x=330,y=200)
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password  ").place(x=250,y=300)
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.place(x=330,y=300)
    Label(login_screen, text="").place(x=300,y=400)
    b1=Button(login_screen, text="Login", width=20, height=2,bd=10, command = login_verify).place(x=450,y=500)
    b2=Button(login_screen, text="Back",width=10,height=2,bd=1,command=home_page)
    b2.place(x=2,y=1)
 
# Implementing event on register button
 

# Implementing event on login button 
 
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
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("1024x800")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
def home_page():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("1024x800")

    #c=Canvas(login_screen,width=1024,height=800,bg="white")
    #c.pack()
    #photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bgss.png')
    #background_label=Label(login_screen,image=photo)
    #background_label.place(x=0,y=0)
    Label(login_screen, text="LOG IN",font="arial 15 bold").place(x=500,y=0)
  
    b1= Button(login_screen, text="DOCTOR LOGIN",font="arial 10 bold",width=20, height=3,bd=10,command=login)
    b1.place(x=450,y=150)
   
    b2=Button(login_screen, text="PATIENT LOGIN", font="arial 10 bold",width=20, height=3,bd=10,command=login)
    b2.place(x=450,y=300)
    main_screen.mainloop()
  





 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1024x800")
    main_screen.title("Health Monitoring System")
    c=Canvas(main_screen,width=1024,height=800,bg="white")
    c.pack()
    photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\health.png')
    background_label=Label(main_screen,image=photo)
    background_label.place(x=300,y=200)
    
    Button(text="Login", height=2, width=10,bd=3, command = home_page).place(x=940,y=0)

    
 
    main_screen.mainloop()
 
 
main_account_screen()
