#inhertiance
"""create a class vehicle with brand name and year"""
#parent class
"""class vehicle:
    def __init__(car,brand,year):
        car.brand=input("enter brand name: ")
        car.year=input("enter year: ")

    def display(car):
        print(car.brand)
        print(car.year)
#child class
class model(vehicle):
    def __init__(car,brand,year):
        vehicle. __init__(car,brand,year)
            
x=model("brand","year")
x.display()"""
#create a class person with age and name
class area:
    def __init__(num,length,width):
        num.length=int(input("enter length:"))
        num.width=int(input("enter width:"))
        
    def __str__(num):
        return f"num.length,num.width"

    def display(num):
        print(num.length)
        print(num.width)
        
class rectangle(area):
    def __init__(num,length,width):
        area.__init__(num,length,width)
        rectangle=num.length*num.width
        print("rectangle:",rectangle)

x=rectangle("length","width")
x.display()
