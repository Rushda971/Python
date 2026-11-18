#movie ticket booking system
"""display a menu of movies and ticket prices.
let user select a movie and number of tickets
calculate and display total price
allow multiple booking until user types "quit"
show final bill at the end."""
print("welcome to bookmyshow")
movies=print("""moives         prices
      1.Raid 2                180-400
      2.Housefull 5           180-400
      3.Bhool chuk maaf       180-400   """)
movie=input("select your moive(1-3): ")
if movie=='1':
    print("Raid2")
elif movie=='2':
    print("Housefull 5")
elif movie=='3':
    print("Bhool chuk maaf")
else:
    print("please enter valid choice(1-3)")
print("Now select your seating!")
print("""seating:
      1.gold
      2.premieum
      3.normal""")
exits=print("if you want to exit,press 4")
user=input("enter seating(1-3):")

if user=='1':
    print("gold")
    price=400
    print("price:",price)
elif user=='2':
    print("silver")
    price=250
    print("price:",price)
elif user=='3':
    print("normal")
    price=180
    print("price:",price)
else:
    print("enter valid choice between (1-3)")
seats=int(input("enter seats for booking:"))    
#calculate billing
print("your bill is: ")
bill=price*seats
print(f"movie:{movie},seats:{seats},bill:{bill}")


