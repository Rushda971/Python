#create class rectangle
class rectangle():
    def __init__(num,length,width):
        num.length=int(input("enter length of rectangle: "))
        num.width=int(input("enter width of rectangle:"))
    def __str__(num):
        return f"num.length,num.width"
    def area(num):
        area=num.length*num.width
        
    
