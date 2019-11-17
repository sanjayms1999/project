from tkinter import *
import os 
window = Tk()
 
window.title("Doctor page")

window.geometry('300x250')
 
tablet=Label(window, text="Tablet :")


mg=Label(window,text="MG :")

timing=Label(window,text="Timing :")

entry1=Entry(window)
entry2=Entry(window)
entry3=Entry(window)


tablet.grid(row=0)
entry1.grid(row=0,column=1)


mg.grid(row=1,column=0)
entry2.grid(row=1,column=1)


timing.grid(row=2,column=0)
entry3.grid(row=2,column=1)
             
c=Button(window,text="Submit")
c.grid(columnspan=3)             
root.mainloop()

