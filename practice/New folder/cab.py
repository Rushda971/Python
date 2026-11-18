#book your ride
class login:
    def __init__(self,name,userid):
        self.name=input("enter your name: ")
        self.userid=input("enter user id: ")
        print(""" 1.driver login
                  2.customer login
                  3.exit""")
        if user==1:


            print("driver login")
            status=print(""" 0.busy
                         1.available""")
            if cab==1:
                print("busy")
            elif cab==2:
                print("available")
                print("soon notify you for ride")


        elif user==2:
            print("customer login")
class book:
    def __init__(self,place):
        self.place=input("enter your destination: ")
        
class ride:
    def __init__(self,book):
        self.book=print("select your ride ")
        print("""
                1.car
                2.bike
                3.auto""")
        user=(int(input("select your choice between(1-3): ")))
        if user==1:
            print("you have choosen car")
            print("")
