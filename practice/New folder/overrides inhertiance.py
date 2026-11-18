#overrides inhertiance
class employee:
    def __init__ (emp,name,role):
        emp.name=input("enter name of employee: ")
        emp.role=input("enter role of employee: ")
        
    def display(emp):
        print(emp.name,emp.role)
        
class position(employee):
   def __init__ (emp,name,role):
       employee.__init__ (emp,name,role)
       emp.post=input("enter position: ")
       
x=position("name","role")
x.display
    
