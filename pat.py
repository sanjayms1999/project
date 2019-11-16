from tkinter import *
 
window = Tk()
 
window.title("Doctor page")
 
window.geometry('550x550')
 
Label(window, text="VIEW ALL PATIENTS").pack()
 
Button(window, text="Patient1",width=20, height=3,bd=10).pack()
 
Button(window, text="Patient2",width=20, height=3,bd=10).pack()


Button(window, text="Patient3",width=20, height=3,bd=10).pack()

Button(window, text="BP Graph",width=20, height=3,bd=10).pack()
Button(window, text="Temp Graph",width=20, height=3,bd=10).pack()

Button(window, text="Search",width=20, height=3,bd=10).pack()

# btn6 = Button(window, text="Back",width=20, height=3,bd=10,command=log_in).pack()

window.mainloop()
