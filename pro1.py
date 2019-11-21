from tkinter import *
from tkinter import ttk
import os


def main_account_screen():

 global main_screen
main_screen= Tk()   # create a GUI window
main_screen.geometry("1024x800") # set the configuration of GUI window 
main_screen.title("Health Monitoring System") # set the title of GUI window



def p_hp():
      global login_screen
      login_screen = Toplevel(main_screen)
      login_screen.title("Health Monitoring System")
      login_screen.geometry("1024x800")

      c=Canvas(login_screen,width=1024,height=800,bg="white")
      c.pack()
      photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bgss.png')
      background_label=Label(login_screen,image=photo)
      background_label.place(x=0,y=0)
   

 
      b1=Button(login_screen,text="LOG OUT",width=10,height=2,bd=1,command=log_in)
      b1.place(x=945,y=0)
      b2 = Button(login_screen, text="Back",width=10, height=2,bd=1,command=log_in)
      b2.place(x=2,y=1)




main_account_screen()

def patient_page():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("1024x800")

    c=Canvas(login_screen,width=1024,height=800,bg="white")
    c.pack()
    photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bgs.png')
    background_label=Label(login_screen,image=photo)
    background_label.place(x=0,y=0)
    
    Label(login_screen, text="Patient Home Page",font="arial 15 bold").place(x=450,y=0)
    Button(login_screen, text="view prescription",width=20, height=3,bd=10,command=p_hp).place(x=400,y=150)
    Button(login_screen, text=" View BP",width=20, height=3,bd=10,command="").place(x=400,y=350)
    Button(login_screen, text="View Temp",width=20, height=3,bd=10,command="").place(x=400,y=550)
    b1=Button(login_screen,text="Log out",width=10,height=2,bd=1,command=log_in)
    b1.place(x=945,y=0)
    b2=Button(login_screen, text="Back",width=10,height=2,bd=1,command=home_page)
    b2.place(x=2,y=1)



def doc_hp():
      global login_screen
      login_screen = Toplevel(main_screen)
      login_screen.title("Health Monitoring System")
      login_screen.geometry("1024x800")

      c=Canvas(login_screen,width=1024,height=800,bg="white")
      c.pack()
      photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bgs.png')
      background_label=Label(login_screen,image=photo)
      background_label.place(x=0,y=0)
      
      
      Label(login_screen, text="DOCTOR HOME PAGE",font="arial 15 bold").place(x=450,y=0)

      l2=Label(login_screen,text="Enter patient Id")
      l2.place(x=30,y=100)
    
      e=Entry(login_screen)
      e.place(x=150,y=100)

      b=Button(login_screen,text="OK")
      b.place(x=180,y=120)

      b=Button(login_screen,text="VIEW ALL",width=20,height=3,bd=10)
      b.place(x=200,y=300)
 

      b1=Button(login_screen,text="LOG OUT",width=10,height=2,bd=1,command=log_in)
      b1.place(x=900,y=0)
      b2=Button(login_screen, text="Back",width=10, height=2,bd=1,command=doctor_page)
      b2.place(x=2,y=1)

def patient_info():
      global login_screen
      login_screen = Toplevel(main_screen)
      login_screen.title("Health Monitoring System")
      login_screen.geometry("1024x800")

      c=Canvas(login_screen,width=1024,height=800,bg="white")
      c.pack()
      photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bgs.png')
      background_label=Label(login_screen,image=photo)
      background_label.place(x=0,y=0)
      
      
 
      Label(login_screen, text="PATIENT DETIALS",font="arial 15 bold").place(x=450,y=0)

      l1=Label(login_screen,text="patient Id")
      l1.place(x=150,y=160)

      e1=Entry(login_screen)
      e1.place(x=230,y=160)


      l2=Label(login_screen,text="patient name")
      l2.place(x=150,y=200)

      e2=Entry(login_screen)
      e2.place(x=230,y=200)

      l3=Label(login_screen,text="Diagnosis")
      l3.place(x=150,y=250)

      e3=Entry(login_screen)
      e3.place(x=230,y=250)



      b1=Button(login_screen,text="Add Prescription",width=20,height=3,bd=10)
      b1.place(x=150,y=400)

      b2=Button(login_screen,text="Log out",width=10,height=2,bd=1,command=log_in)
      b2.place(x=945,y=0)
      b3 = Button(login_screen, text="Back",width=10, height=2,bd=1,command=doctor_page)
      b3.place(x=2,y=1)

def prescrip():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("1024x800")

    c=Canvas(login_screen,width=1024,height=800,bg="white")
    c.pack()
    photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bgs.png')
    background_label=Label(login_screen,image=photo)
    background_label.place(x=0,y=0)
   
    
      
     

    Label(login_screen, text="PRESRIP",font="arial 15 bold").pack()

    l1=Label(login_screen,text="Med Name")
    l1.place(x=150,y=150)

    e1=Entry(login_screen)
    e1.place(x=230,y=150)


    l2=Label(login_screen,text="MG")
    l2.place(x=150,y=200)

    e2=Entry(login_screen)
    e2.place(x=230,y=200)

    l3=Label(login_screen,text="Timings")
    l3.place(x=150,y=250)

    e3=Entry(login_screen)
    e3.place(x=230,y=250)




    b1=Button(login_screen,text="Submit",width=20,height=3,bd=10)
    b1.place(x=150,y=400)

    b2=Button(login_screen,text="Log out",width=10,height=2,bd=1,command=doctor_page)
    b2.place(x=945,y=0)
    b3 = Button(login_screen, text="Back",width=10, height=2,bd=1,command=log_in)
    b3.place(x=2,y=1)

def doctor_page():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("1024x800")

    c=Canvas(login_screen,width=1024,height=800,bg="white")
    c.pack()
    photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bgs.png')
    background_label=Label(login_screen,image=photo)
    background_label.place(x=0,y=0)
   

    Label(login_screen, text="DOCTOR HOMEPAGE",font="arial 15 bold").place(x=450,y=0)
    Button(login_screen, text="Doctor HP",width=20,height=3,bd=10,command=doc_hp).place(x=400,y=150)
    Button(login_screen, text="Patient Info",width=20,height=3,bd=10,command=patient_info).place(x=400,y=350)
    Button(login_screen, text="Prescrip",width=20,height=3,bd=10,command=prescrip).place(x=400,y=550)
    Button(login_screen, text="Back",width=10,height=2,bd=1,command=home_page).place(x=0,y=0)



    
main_account_screen()

def log_in():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("1024x800")

    c=Canvas(login_screen,width=1024,height=800,bg="white")
    c.pack()
    photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bgss.png')
    background_label=Label(login_screen,image=photo)
    background_label.place(x=0,y=0)
    Label(login_screen, text="Please enter details below to login").place(x=450,y=0)
    #Label(login_screen, text="").pack()
   
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
    Button(login_screen, text="Login", width=20, height=2,bd=10 ,command =patient_page).place(x=450,y=500)
 
    b1=Button(login_screen, text="Back", width=10, height=2 ,command = home_page)
    b1.place(x=2,y=1)

 
    
    main_screen.mainloop()




def doctor_page():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("1024x800")

    c=Canvas(login_screen,width=1024,height=800,bg="white")
    c.pack()
    photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bgss.png')
    background_label=Label(login_screen,image=photo)
    background_label.place(x=0,y=0)
   

    Label(login_screen, text="DOCTOR HOMEPAGE",font="arial 15 bold").place(x=450,y=0)
    Button(login_screen, text="Doctor HP",width=20,height=3,bd=10,command=doc_hp).place(x=400,y=150)
    Button(login_screen, text="Patient Info",width=20,height=3,bd=10,command=patient_info).place(x=400,y=350)
    Button(login_screen, text="Prescrip",width=20,height=3,bd=10,command=prescrip).place(x=400,y=550)
    Button(login_screen, text="Back",width=10,height=2,bd=1,command=home_page).place(x=0,y=0)



    


def patient_page():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("1024x800")

    c=Canvas(login_screen,width=1024,height=800,bg="white")
    c.pack()
    photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bgss.png')
    background_label=Label(login_screen,image=photo)
    background_label.place(x=0,y=0)
    
    Label(login_screen, text="Patient Home Page",font="arial 15 bold").place(x=450,y=0)
    Button(login_screen, text="view prescription",width=20, height=3,bd=10,command=p_hp).place(x=400,y=150)
    Button(login_screen, text=" View BP",width=20, height=3,bd=10,command="").place(x=400,y=350)
    Button(login_screen, text="View Temp",width=20, height=3,bd=10,command="").place(x=400,y=550)
    b1=Button(login_screen,text="Log out",width=10,height=2,bd=1,command=log_in)
    b1.place(x=945,y=0)
    b2=Button(login_screen, text="Back",width=10,height=2,bd=1,command=home_page)
    b2.place(x=2,y=1)


    main_screen.mainloop()

    
def home_page():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("1024x800")

    c=Canvas(login_screen,width=1024,height=800,bg="white")
    c.pack()
    photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\bgss.png')
    background_label=Label(login_screen,image=photo)
    background_label.place(x=0,y=0)
    Label(login_screen, text="LOG IN",font="arial 15 bold").place(x=500,y=0)
  
    b1= Button(login_screen, text="DOCTOR LOGIN",width=20, height=3,bd=10,command=log_in)
    b1.place(x=450,y=150)
   
    b2=Button(login_screen, text="PATIENT LOGIN", width=20, height=3,bd=10,command=log_in)
    b2.place(x=450,y=300)
    main_screen.mainloop()
  

       

b1=Button(main_screen, text="Login", command=home_page).pack()
c=Canvas(main_screen,width=1024,height=800,bg="white")
c.pack()
photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\health.png')
background_label=Label(main_screen,image=photo)
background_label.place(x=320,y=200)
    

#b1.place(x=945,y=0)


main_screen.mainloop()


    




    
main_account_screen()
 
