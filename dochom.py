from tkinter import *
 
window = Tk()
 
window.title("Doctor page")
 
window.geometry('550x550')
#def ok():
   # patient Id=e.get()
    #l3.configure(text="".format(patient Id))
Label(window, text="DOCTOR HOME PAGE",font="arial 15 bold").pack()

l2=Label(window,text="Enter patient Id")
l2.place(x=30,y=100)

e=Entry()
e.place(x=120,y=100)

b=Button(window,text="OK")
b.place(x=180,y=120)

b=Button(window,text="VIEW ALL",width=20,height=3,bd=10)
b.place(x=200,y=300)
# btn6 = Button(window, text="Back",width=20, height=3,bd=10,command=log_in).pack()

window.mainloop()
