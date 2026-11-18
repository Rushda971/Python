"""Real-Life Practice Task: Job Application Form
🧠 Scenario:
Create a Job Application Form GUI for a company. The applicant will:
Enter their Full Name and Email Address.
Choose their Gender.
Select their Skills (multiple options like Python, Excel, Communication, etc.).
Pick their Preferred Department (from a Listbox).
Click Submit to see the entered data printed (or saved).
"""
from tkinter import *
root=Tk()
root.title("Job Application")
Label(root,text="Name:").grid(row=0)
Label(root,text="Email:").grid(row=1)
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
var=IntVar()
Radiobutton(root,text="Male",variable=var,value=1).grid()
Radiobutton(root,text="Female",variable=var,value=2).grid()
Label(root,text="Select Skill")
a=Listbox(root)
a.insert(1,"Communication")
a.insert(2,"Excel")
a.insert(3,"Python")
a.insert(4,"more")
button=Button(root,text="Submit",command=root.destroy)
button.grid()
mainloop()