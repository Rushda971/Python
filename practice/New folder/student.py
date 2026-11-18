#student admission
class student:
    def ___init__(self,name,std,grade):
        self.name=input("enter student name: ")
        self.std=input("enter course want to purse: ")
        self.grade=int(input("enter grade score: "))

    def __str__(self):
        return f"{self.name},{self.std},self.grade"

    def display(self):
        print("name:",self.name)
        print("std: ",self.std)
        print("grade:",self.grade)

