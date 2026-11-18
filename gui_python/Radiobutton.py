from tkinter import *
root=Tk()
Var1=IntVar()
Radiobutton(root,text="Male",variable=Var1,value=1).pack()
Radiobutton(root,text="Female",variable=Var1,value=2).pack()
mainloop()