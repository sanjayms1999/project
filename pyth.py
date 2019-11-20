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
   

 
    b1=Button(php_screen,text="LOG OUT",width=10,height=2,bd=1)
    b1.place(x=945,y=0)
    b2 = Button(php_screen, text="Back",width=10, height=2,bd=1,command=patient_page)
    b2.place(x=2,y=1)




main_account_screen()

def patient_page():
    
    patient_screen=Toplevel(main_screen)
    patient_screen.geometry("1024x800")
    
    #hms=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bg1.gif')
    #label=ttk.Label(patient_screen,image=hms)
    #PhotoImage(file='C:\\Users\\Admin\\Desktop\\bg1.gif')
    #label.pack()

    patient_screen.title("Health Monitoring System")
    Label(patient_screen, text="Patient Home Page",font="arial 15 bold").pack(pady=10)
    Button(patient_screen, text="view prescription",width=20, height=3,bd=10,command=p_hp).pack(pady=20)
    
    Button(patient_screen, text=" View BP",width=20, height=3,bd=10,command="").pack(pady=20)
    Button(patient_screen, text="View Temp",width=20, height=3,bd=10,command="").pack(pady=20)
    b1=Button(patient_screen,text="Log out",width=10,height=2,bd=1)
    b1.place(x=945,y=0)
    b2=Button(patient_screen, text="Back",width=10,height=2,bd=1,command=home_page)
    b2.place(x=2,y=1)



def doc_hp():
      doctor_screen=Toplevel(main_screen)
      doctor_screen.geometry("1024x800")
      doctor_screen.title("Health Monitoring System")
      
      Label(doctor_screen, text="DOCTOR HOME PAGE",font="arial 15 bold").pack()

      l2=Label(doctor_screen,text="Enter patient Id")
      l2.place(x=30,y=100)

      e=Entry(doctor_screen)
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

      e1=Entry(patient_screen)
      e1.place(x=230,y=160)


      l2=Label(patient_screen,text="patient name")
      l2.place(x=150,y=200)

      e2=Entry(patient_screen)
      e2.place(x=230,y=200)

      l3=Label(patient_screen,text="Diagnosis")
      l3.place(x=150,y=250)

      e3=Entry(patient_screen)
      e3.place(x=230,y=250)



      b1=Button(patient_screen,text="Add Prescription",width=20,height=3,bd=10)
      b1.place(x=150,y=400)

      b2=Button(patient_screen,text="Log out",width=10,height=2,bd=1)
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

     e1=Entry(prescrip_screen)
     e1.place(x=230,y=150)


     l2=Label(prescrip_screen,text="MG")
     l2.place(x=150,y=200)

     e2=Entry(prescrip_screen)
     e2.place(x=230,y=200)

     l3=Label(prescrip_screen,text="Timings")
     l3.place(x=150,y=250)

     e3=Entry(prescrip_screen)
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
    Button(doctor_screen, text="Patient Info",width=20,height=3,bd=10,command=patient_info).pack(pady=20)
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
 
    Label(login_screen, text="User ID ").place(x=250,y=200)
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.place(x=330,y=200)
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password ").place(x=250,y=300)
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.place(x=330,y=300)
    Label(login_screen, text="").place(x=300,y=400)
    Button(login_screen, text="Login", width=20, height=2,bd=10 ,command = patient_page).place(x=450,y=500)
 
    b1=Button(login_screen, text="Back", width=10, height=2 ,command = home_page)
    b1.place(x=2,y=1)
    main_screen.mainloop()



    
def home_page():
    screen=Toplevel(main_screen)
    screen.geometry("1024x800")
    

    Label(screen, text="LOG IN",font="arial 15 bold").pack()
    Label(screen, text="").pack()
    b1= Button(screen, text="DOCTOR LOGIN",width=20, height=3,bd=10,command=log_in)
    b1.pack(pady=50)
   
    b2=Button(screen, text="PATIENT LOGIN", width=20, height=3,bd=10,command=log_in)
    b2.pack(pady=50)
    c=Canvas(screen,width=1024,height=800,bg="white")
    c.pack()
    photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\health.png')
    background_label=Label(screen,image=photo)
    background_label.place(x=0,y=0)
  


       

b1=Button(main_screen, text="Login", command=home_page).pack()

#b1.place(x=945,y=0)

c=Canvas(main_screen,width=1024,height=800,bg="white")
c.pack()
photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\health.png')
background_label=Label(main_screen,image=photo)
background_label.place(x=300,y=200)
    

    
main_screen.mainloop()


    




    
main_account_screen()
 
