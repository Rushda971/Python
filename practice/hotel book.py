print("Welcome to the hotel!")
guest = int(input("Number of guests: "))
days = int(input("Number of days to stay: "))

def room():
    print("""
Type of room:
1. Single
2. Double
3. Deluxe
4. Exit
""")
    user = int(input("Choose room type (1-4): "))
    if user == 1:
        print("Single Room:\n- Air conditioning\n- Private bathroom\n- Free WiFi, etc.")
        return 2000
    elif user == 2:
        print("Double Room:\n- 1 extra-large double bed\n- Air conditioning\n- Free WiFi, etc.")
        return 3500
    elif user == 3:
        print("Deluxe Room:\n- 1 extra-large double bed\n- All deluxe amenities.")
        return 5000
    elif user == 4:
        print("Exiting booking system.")
        return -1  # Special value to signal exit
    else:
        print("Please enter a valid number (1-4).")
        return 0  # Invalid input

def calculate(price_per_day, days):
    bill = price_per_day * days
    print("Your bill: ₹", bill)

# Main Loop
while True:
    price = room()
    if price == -1:
        break
    elif price == 0:
        continue
    else:
        calculate(price, days)
