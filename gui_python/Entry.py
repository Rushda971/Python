from tkinter import *
a=Tk()
Label(a,text="admin").grid(row=0)
Label(a,text="password").grid(row=1)
a1=Entry(a)
a2=Entry(a)
a1.grid(row=0,column=1)
a2.grid(row=1,column=1)
mainloop()