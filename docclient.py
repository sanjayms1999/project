from tkinter import *
 
window = Tk()
 
window.title("Health Monitoring system")
 
window.geometry('1024x800')

Label(window, text="PATIENT DETIALS",font="arial 15 bold").pack()

l1=Label(window,text="patient Id")
l1.place(x=150,y=160)

e1=Entry()
e1.place(x=230,y=160)


l2=Label(window,text="patient name")
l2.place(x=150,y=200)

e2=Entry()
e2.place(x=230,y=200)

l3=Label(window,text="Diagnosis")
l3.place(x=150,y=250)

e3=Entry()
e3.place(x=230,y=250)



b1=Button(window,text="Add Prescription",width=20,height=3,bd=10)
b1.place(x=150,y=400)

b2=Button(window,text="Log out",width=20,height=3,bd=10)
b2.place(x=750,y=400)
#b3 = Button(window, text="Back",width=20, height=3,bd=10,command=log_in).pack()

window.mainloop()
