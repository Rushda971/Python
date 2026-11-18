#object and class
class person:
    def __init__(self,age,name):
        self.age=int(input("enter your age:"))
        if self.age>18:
            print("Adult")
        else:
            print("minor")
        self.name=input("enter your name:")
    def __str__(self):
        return f"self.age,{self.name}"
    def display(self):
        print("age:",self.age)
        print("name:",self.name)
x=person("age","name")
x.display()
#create class rectangle
"""constructor should take length and width
method area() should return the area"""
class rectangle():
    def __init__(num,length,width):
        num.length=int(input("enter length of rectangle: "))
        num.width=int(input("enter width of rectangle:"))
        #num.area=num.length*num.width
    def __str__(num):
        return f"num.length,num.width,area"
    def display(num):
        print("length",num.length)
        print("width",num.width)
        area=num.length*num.width
        print("area",area)
x=rectangle("length","width")
x.display()
        
        
