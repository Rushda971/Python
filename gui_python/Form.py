""" 1. User Info Form
Goal:
Create a form with:
A Label and Entry for Name
A Label and Entry for Email
A Checkbutton to agree to "I accept terms & conditions"
A Button labeled "Submit"
📌 When the button is clicked:
If the checkbox is checked, print name and email.
If not checked, show a message like "Please accept terms to continue."
"""
from tkinter import *
def submit():
    if var1.get()==1:
        name=e1.get()
        email=e2.get()
        result_label.config(text=f"Name: {name}\nEmail: {email}", fg="green")
    else:
        result_label.config(text="Please accept terms and condition", fg="red")
 
a=Tk()
a.title("Form")
Label(a,text="Name").grid(row=0)
Label(a,text="Email").grid(row=1)
e1=Entry(a)
e2=Entry(a)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
var1=IntVar()
Checkbutton(a,text="I accept all term and condition",variable=var1).grid(row=2)
button=Button(a,text="submit",command=submit)
button.grid()


mainloop()

