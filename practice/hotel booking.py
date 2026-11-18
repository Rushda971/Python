#hotel room booking system
#
print("welcome to hotel")
guest=int(input("number of guest: "))
room=("""type of room:
      1.single
      2.double
      3.deluxe
      4.exit""")
days=int(input("no.of day stay : "))
print(room)
user=int(input("please enter number (1-4):"))
def room():
    if user==1:
        print("""single room:
        Air conditioning
        Private bathroom
        Flat-screen
        TV
        Free WiFi
        Free toiletries
        Toilet
        Towels
        Linen
        Socket near the bed Tile
        marble floor Desk Seating Area
        Telephone
        Tea/Coffee maker Fan Electric
        kettle Cable channels Wardrobe or closet Upper floors accessible by elevator
        Clothes rack
        Toilet paper""")
        price="RS.2000"
        print(price)
    elif user==2:
        print("""1 extra-large double bed 
        Air conditioning
        Private bathroom
        Flat-screen
        TV
        Free WiFi
        Free toiletries
        Toilet
        Towels
        Linen
        Socket near the bed Tile
        marble floor Desk Seating Area
        Telephone
        Tea/Coffee maker Fan Electric
        kettle Cable channels Wardrobe or closet Upper floors accessible by elevator
        Clothes rack
        Toilet paper """)
        price="RS.3500"
        print(price)
    elif user==3:
        print("""1 extra-large double bed 
        Air conditioning
        Private bathroom
        Flat-screen
        TV
        Free WiFi
        Free toiletries
        Toilet Towels
        Linen Socket near the bed Tile
        marble floor Desk Seating Area Telephone Tea
        Coffee maker Fan Electric kettle Cable channels Wardrobe or
        closet Upper floors accessible by elevator Clothes rack Toilet paper """)
        price="RS.5000"
        print(price)
    elif user==4:
        print("sure you want to exit?")
        #break
    else:
        print("please enter valid no.(1-4)")
def calculate():
    bill=price*days
    print("your bill:",bill)
room()
calculate()
