import tkinter as tk
root=tk.Tk()
root.title("Application form")
root.geometry("500x400")
name_var=tk.StringVar()
name_entry=tk.Entry(root,textvariable=name_var)
name_entry.grid(column=1,row=0)
text_var=tk.StringVar()
email_entry=tk.Entry(root,textvariable=text_var)
email_entry.grid(column=1,row=1)
data=''
def sumbits():
    name=name_entry.get()
    email=email_entry.get()
    data=name+" "+email
    print("form detail:\n name:  ",name,"email: ",email)
    output=tk.Label(root,text=data) 
    output.grid(column=1,row=4) 
 
btn=tk.Button(root,text='submit', command=sumbits)
btn.grid(column=1,row=3)
root.mainloop()