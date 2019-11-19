from tkinter import *
from tkinter import ttk
import os

def main_account_screen():

 global main_screen
main_screen= Tk()   # create a GUI window
main_screen.geometry("1024x800") # set the configuration of GUI window 
main_screen.title("Health Monitoring System") # set the title of GUI window


def p_hp():
    php_screen=Toplevel(main_screen)
    php_screen.geometry("1024x800")
    php_screen.title("Health Monitoring System")
    Label( php_screen, text="PATIENT HOME PAGE",font="arial 15 bold").pack()

    b1=Button(php_screen,text="VIEW PRESCRIPTION",width=20,height=3,bd=10)
    b1.place(x=450,y=300)
    b2=Button(php_screen,text="VIEW GRAPH",width=20,height=3,bd=10)
    b2.place(x=450,y=500)
    b3=Button(php_screen,text="LOG OUT",width=10,height=2,bd=1)
    b3.place(x=945,y=0)
    b4 = Button(php_screen, text="Back",width=10, height=2,bd=1,command=patient_page)
    b4.place(x=2,y=1)


    

def graph_info():
    graph_screen=Toplevel(main_screen)
    graph_screen.geometry("1024x800")
    graph_screen.title("Health Monitoring System")
    
    b1=Button(graph_screen,text="VIEW BP",width=20,height=3,bd=10)
    b1.place(x=450,y=300)
    b2=Button(graph_screen,text="VIEW TEMP",width=20,height=3,bd=10)
    b2.place(x=450,y=500)
    b3=Button(graph_screen,text="LOG OUT",width=10,height=2,bd=1)
    b3.place(x=945,y=0)
    b4 = Button(graph_screen, text="Back",width=10, height=2,bd=1,command=patient_page)
    b4.place(x=2,y=1)

def bp_info():
    bp_screen=Toplevel(main_screen)
    bp_screen.geometry("1024x800")
    bp_screen.title("Health Monitoring System")
    b1=Button(bp_screen,text="VIEW BP",width=20,height=3,bd=10)
    b1.place(x=450,y=300)
    b2=Button(bp_screen,text="LOG OUT",width=10,height=2,bd=1)
    b2.place(x=945,y=0)
    b3 = Button(bp_screen, text="Back",width=10, height=2,bd=1,command=patient_page)
    b3.place(x=2,y=1)


def temp_info():
     temp_screen=Toplevel(main_screen)
     temp_screen.geometry("1024x800")
     temp_screen.title("Health Monitoring System")

     b1=Button(temp_screen,text="VIEW TEMP",width=20,height=3,bd=10)
     b1.place(x=450,y=300)
     b2=Button(temp_screen,text="LOG OUT",width=10,height=2,bd=1)
     b2.place(x=945,y=0)
     b3 = Button(temp_screen, text="Back",width=10, height=2,bd=1,command=patient_page)
     b3.place(x=2,y=1)


main_account_screen()

def patient_page():
    
    patient_screen=Toplevel(main_screen)
    patient_screen.geometry("500x350")
    
    hms=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bg1.gif')
    label=ttk.Label(patient_screen,image=hms)
    PhotoImage(file='C:\\Users\\Admin\\Desktop\\bg1.gif')
    label.pack()

    patient_screen.title("Health Monitoring System")
    Label(patient_screen, text="Patient Page",font="arial 15 bold").pack(pady=10)
    Button(patient_screen, text="Patient HP",width=20, height=3,bd=10,command=p_hp).pack(pady=20)
    Button(patient_screen, text="Graph",width=20, height=3,bd=10,command=graph_info).pack(pady=20)
    Button(patient_screen, text="BP",width=20, height=3,bd=10,command=bp_info).pack(pady=20)
    Button(patient_screen, text="Temp",width=20, height=3,bd=10,command=temp_info).pack(pady=20)
    b1=Button(patient_screen, text="Back",width=10,height=2,bd=1,command=home_page)
    b1.place(x=2,y=1)



def doc_hp():
      doctor_screen=Toplevel(main_screen)
      doctor_screen.geometry("1024x800")
      doctor_screen.title("Health Monitoring System")
      
      Label(doctor_screen, text="DOCTOR HOME PAGE",font="arial 15 bold").pack()

      l2=Label(doctor_screen,text="Enter patient Id")
      l2.place(x=30,y=100)

      e=Entry()
      e.place(x=150,y=100)

      b=Button(doctor_screen,text="OK")
      b.place(x=180,y=120)

      b=Button(doctor_screen,text="VIEW ALL",width=20,height=3,bd=10)
      b.place(x=200,y=300)
 

      b1=Button(doctor_screen,text="LOG OUT",width=10,height=2,bd=1)
      b1.place(x=945,y=0)
      b2=Button(doctor_screen, text="Back",width=10, height=2,bd=1,command=doctor_page)
      b2.place(x=2,y=1)
      
def patient_info():
      patient_screen=Toplevel(main_screen)
      patient_screen.geometry("1024x800")
      patient_screen.title("Health Monitoring System")
 
      Label(patient_screen, text="PATIENT DETIALS",font="arial 15 bold").pack()

      l1=Label(patient_screen,text="patient Id")
      l1.place(x=150,y=160)

      e1=Entry()
      e1.grid(row=2,column=3)


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

      b2=Button(patient_screen,text="Log out",width=10,height=3,bd=1)
      b2.place(x=945,y=0)
      b3 = Button(patient_screen, text="Back",width=10, height=2,bd=1,command=doctor_page)
      b3.place(x=2,y=1)

def prescrip():
     prescrip_screen=Toplevel(main_screen)
     prescrip_screen.geometry("1024x800")
     prescrip_screen.title("Health Monitoring System")

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

     b2=Button(prescrip_screen,text="Log out",width=10,height=2,bd=1)
     b2.place(x=945,y=0)
     b3 = Button(prescrip_screen, text="Back",width=10, height=2,bd=1,command=doctor_page)
     b3.place(x=2,y=1)

def doctor_page():
    doctor_screen=Toplevel(main_screen)
    doctor_screen.geometry("1024x800")
    doctor_screen.title("Health Monitoring System")
    Label(doctor_screen, text="DOCTOR HOMEPAGE",font="arial 15 bold").pack(pady=10)
    Button(doctor_screen, text="Doctor HP",width=20,height=3,bd=10,command=doc_hp).pack(pady=20)
    Button(doctor_screen, text="Patient info",width=20,height=3,bd=10,command=patient_info).pack(pady=20)
    Button(doctor_screen, text="Prescrip",width=20,height=3,bd=10,command=prescrip).pack(pady=20)
    Button(doctor_screen, text="Back",width=20,height=3,bd=10,command=home_page).pack(pady=20)
    
main_account_screen()

def log_in():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
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
    Button(login_screen, text="Login", width=10, height=1, command = doctor_page or patient_page).pack(pady=30)
 
    b1=Button(login_screen, text="Back", width=10, height=1,bd=1 ,command = home_page)
    b1.place(x=2,y=1)
    main_screen.mainloop()

    
def home_page():
    screen=Toplevel(main_screen)
    screen.geometry("1024x800")
    Label(screen, text="LOG IN",font="arial 15 bold").pack()
    Label(screen, text="").pack()
    b1= Button(screen, text="DOCTOR LOGIN",width=20, height=3,bd=10,command=log_in).pack(pady=50)
   
    b2=Button(screen, text="PATIENT LOGIN", width=20, height=3,bd=10,command=log_in).pack(pady=50)
  


    hms=PhotoImage(file='C:\\Users\\Admin\\Desktop\\HMS1.gif')
    label=ttk.Label(screen,image=hms)
    PhotoImage(file='C:\\Users\\Admin\\Desktop\\HMS1.gif')
    label.pack()

    

b1=Button(main_screen, text="Login", width=10, height=1, command=home_page)
b1.place(x=945,y=0)
    


    
main_screen.mainloop()


    




    
main_account_screen()
 
