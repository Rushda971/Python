#inhertiance:parent class
class schoolmember:
    def __init__(self,name,age):
        self.name=input("enter your name: ")
        self.age=int(input("enter your age: "))
    def __str__(self):
        return f"{self.name},{self.age}"
    def display(self):
        print(f"name:{self.name},age:{self.age}")
#child class
class ids(schoolmember):
    def __init__(self,name,age,grade,rollno):
        super().__init__(name,age)
        self.grade=input("enter your grade: ")
        self.rollno=int(input("enter your rollno: "))
    def __str__(self):
        return f"{self.grade},{self.rollno}"
    def display(self):
        print(f"name:{self.name},age:{self.age},grade:{self.grade},rollno:{self.rollno}")
x=ids("name","age","grade","rollno")
x.display()
              
        
        
        
