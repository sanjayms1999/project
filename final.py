from tkinter import *
from tkinter import ttk
import os

def main_account_screen():

 global main_screen
main_screen= Tk()   # create a GUI window
main_screen.geometry("1024x800") # set the configuration of GUI window 
main_screen.title("Health Monitoring System") # set the title of GUI window
("HMS1.gif")

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
    Button(doctor_screen, text="Doc HP",width=10,height=2,command=doc_hp).pack(pady=10)
    Button(doctor_screen, text="Patient info",width=10,height=2,command=patient_info).pack(pady=10)
    Button(doctor_screen, text="Prescrip",width=10,height=2,command=prescrip).pack(pady=10)
    Button(doctor_screen, text="Back",width=10,height=2,command=home_page).pack(pady=10)
    
    
def doc_hp():
      doctor_screen=Toplevel(main_screen)
      doctor_screen.geometry("1024x800")
      Label(window, text="DOCTOR HOME PAGE",font="arial 15 bold").pack()

      l2=Label(doctor_screen,text="Enter patient Id")
      l2.place(x=30,y=100)

      e=Entry()
      e.place(x=120,y=100)

      b=Button(doctor_screen,text="OK")
      b.place(x=180,y=120)

      b=Button(doctor_screen,text="VIEW ALL",width=20,height=3,bd=10)
      b.place(x=200,y=300)
 

      b1=Button(doctor_screen,text="LOG OUT",width=20,height=3,bd=10)
      b1.place(x=750,y=300)
      b2=Button(doctor_screen, text="Back",width=20, height=3,bd=10,command=doctor_page).pack()

def patient_info():
      patient_screen=Toplevel(main_screen)
      patient_screen.geometry("1024x800")
      
 
      Label(patient_screen, text="PATIENT DETIALS",font="arial 15 bold").pack()

      l1=Label(patient_screen,text="patient Id")
      l1.place(x=150,y=160)

      e1=Entry()
      e1.place(x=230,y=160)


      l2=Label(patient_screen,text="patient name")
      l2.place(x=150,y=200)

      e2=Entry()
      e2.place(x=230,y=200)

      l3=Label(patient_screen,text="Diagnosis")
      l3.place(x=150,y=250)

      e3=Entry()
      e3.place(x=230,y=250)



      b1=Button(patient_screen,text="Add Prescription",width=20,height=3,bd=10)
      b1.place(x=150,y=400)

      b2=Button(patient_screen,text="Log out",width=20,height=3,bd=10)
      b2.place(x=750,y=400)
      b3 = Button(patient_screen, text="Back",width=20, height=3,bd=10,command=doctor_page).pack()


def prescrip():
     prescrip_screen=Toplevel(main_screen)
     prescrip_screen.geometry("1024x800")

     Label(prescrip_screen, text="PRESRIP",font="arial 15 bold").pack()

     l1=Label(prescrip_screen,text="Med Name")
     l1.place(x=150,y=150)

     e1=Entry()
     e1.place(x=230,y=150)


     l2=Label(prescrip_screen,text="MG")
     l2.place(x=150,y=200)

     e2=Entry()
     e2.place(x=230,y=200)

     l3=Label(prescrip_screen,text="Timings")
     l3.place(x=150,y=250)

     e3=Entry()
     e3.place(x=230,y=250)



     b1=Button(prescrip_screen,text="Submit",width=20,height=3,bd=10)
     b1.place(x=150,y=400)

     b2=Button(prescrip_screen,text="Log out",width=20,height=3,bd=10)
     b2.place(x=750,y=400)
     b3 = Button(prescrip_screen, text="Back",width=20, height=3,bd=10,command=doctor_page).pack()


def patient_home():
    patient_screen=Toplevel(main_screen)
    patient_screen.geometry("500x350")
    Label(patient_screen, text="Patient Page").pack()
    Button(patient_screen, text="patient Hp",width=20, height=3,bd=10,command=p_hp).pack()
    Button(patient_screen, text="graph",width=20, height=3,bd=10,command=graph_info).pack()
   
    Button(cus_screen, text="Back",width=10,height=2,command=home_page).pack()


def p_hp():
    php_screen=Toplevel(main_screen)
    php_screen.geometry("1024x800")
    Label( php_screen, text="PATIENT HOME PAGE",font="arial 15 bold").pack()

    b1=Button(php_screen,text="VIEW PRESCRIPTION",width=20,height=3,bd=10)
    b1.place(x=150,y=100)
    b2=Button(php_screen,text="VIEW GRAPH",width=20,height=3,bd=10)
    b2.place(x=750,y=100)
    b3=Button(php_screen,text="LOG OUT",width=20,height=3,bd=10)
    b3.place(x=750,y=300)
    b4 = Button(php_screen, text="Back",width=20, height=3,bd=10,command=patient_page)
    b4.place(x=150,y=300)


    

def graph_info():
    graph_screen=Toplevel(main_screen)
    graph_screen.geometry("1024x800")

    
    b1=Button(graph_screen,text="VIEW BP",width=20,height=3,bd=10)
    b1.place(x=150,y=100)
    b2=Button(graph_screen,text="VIEW TEMP",width=20,height=3,bd=10)
    b2.place(x=750,y=100)
    b3=Button(graph_screen,text="LOG OUT",width=20,height=3,bd=10)
    b3.place(x=750,y=300)
    b4 = Button(graph_screen, text="Back",width=20, height=3,bd=10,command=patient_page)
    b4.place(x=150,y=300)


    
main_account_screen()
 
