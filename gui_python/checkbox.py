from tkinter import *
a=Tk()
var1=IntVar()
Checkbutton(a,text="male",variable=var1).grid(row=0)
var2=IntVar()
Checkbutton(a,text="female",variable=var2).grid(row=1)
mainloop()