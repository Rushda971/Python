#hospital appointment booking system
"""show list of doctors with available slot
#user can choose a doctor and book an appointment
#prevent double booking
#optinally cancel or change appointment"""
import datetime
x=datetime.datetime.now()
print(x.strftime("%X"))
print("welcome to hospital appointment booking system")
book=[]
def doctor():
    doctors = {
        "1.Dr. Priya Sharma": {
            "Specialty": "General Physician",
            "Slots": ["10:00 AM", "11:00 AM", "2:00 PM"]
        },
        "2.Dr. Arjun Mehta": {
            "Specialty": "Dentist",
            "Slots": ["9:00 AM", "12:00 PM", "3:00 PM"]
        },
        "3.Dr. Neha Kapoor": {
            "Specialty": "Pediatrician",
            "Slots": ["11:30 AM", "1:00 PM", "4:30 PM"]
        },
        "4.Dr. Rohit Verma": {
            "Specialty": "Orthopedic",
            "Slots": ["10:30 AM", "1:30 PM", "5:00 PM"]
        },
        "5.Dr. Ayesha Khan": {
            "Specialty": "Dermatologist",
            "Slots": ["10:00 AM", "12:30 PM", "3:30 PM"]
        },
        "6.Dr. Rajiv Nair": {
            "Specialty": "Cardiologist",
            "Slots": ["9:00 AM", "1:00 PM", "4:00 PM"]
        }
    }
    for x in doctors:
        print(x)
user=input("please enter your name: ")
cancel=input("sure you want to exit: ")
"""if cancel=="yes":
    exit
else:
    continue"""
def booking():
    user=input("please enter doctors(1-6):")
    if user=="1":
        print("Dr. Priya Sharma")
        print("Specialty:General Physician")
        Slot=["10:00 AM","11:00 AM","2:00PM"]
        print(Slot)
        user=input("choose you slot for booking:")
        doctors=Slot.remove(user)
        print("your appointment has book successfully")
        Slot.append(book)
        print(book)
    elif user=="2":
        print("Dr. Arjun Mehta")
        print("Specialty:Dentist")
        Slot=["9:00 AM", "12:00 PM", "3:00 PM"]
        print(Slot)
        user=input("choose you slot for booking:")
        doctors=Slot.remove(user)
        print("your appointment has book successfully")
        Slot.append(book)
        print(book)
    elif user=="3":
        print("Dr. Neha Kapoor")
        print("Specialty:Pediatrician")
        Slot=["11:30 AM", "1:00 PM", "4:30 PM"] 
        print(Slot)
        user=input("choose you slot for booking:")
        doctors=Slot.remove(user)
        print("your appointment has book successfully")
        Slot.append(book)
        print(book)
    elif user=="4":
        print("Dr. Rohit Verma")
        print("Specialty:Orthopedic")
        Slot=["10:30 AM", "1:30 PM", "5:00 PM"]
        print(Slot)
        user=input("choose you slot for booking:")
        doctors=Slot.remove(user)
        print("your appointment has book successfully")
        Slot.append(book)
        print(book)
    elif user=="5":
        print("Dr. Ayesha Khan")
        print("Specialty:Dermatologist")
        Slot=["10:00 AM", "12:30 PM", "3:30 PM"]
        print(Slot)
        user=input("choose you slot for booking:")
        doctors=Slot.remove(user)
        print("your appointment has book successfully")
        Slot.append(book)
        print(book)
    elif user=="6":
        print("Dr. Rajiv Nair")
        print("Specialty:Cardiologist")
        Slot= ["9:00 AM", "1:00 PM", "4:00 PM"]
        print(Slot)
        user=input("choose you slot for booking:")
        doctors=Slot.remove(user)
        print("your appointment has book successfully")
        Slot.append(book)
        print(book)
    else:
        print("please enter your valid number(1-6)")
         
def cancel():
    cancel="sure you want to cancel ??"
    print(cancel)
    doctors=Slot.append(user)
    print("your slot has successfully cancel")
    exit
while True:
    doctor()
    booking()
    if user==0:
        cancel()
    

    
    
    
