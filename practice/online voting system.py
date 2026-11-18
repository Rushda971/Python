print("welcome to voting system managed by election commission of india")
#login
def login():
    print("Login")
    print("1.Indian resident")
    print("2.Indian Oversea electors")
    user=int(input("enter your choice 1 or 2:"))
    if user==1:
        print("Indian resident")
        user=int(input("Enter registered mobile no: "))
        password=int(input("Enter password:"))
        print("Forget password")
    elif user==2:
         print("Indian Oversea electors")
         user=int(input("Enter registered mobile no: "))
         password=int(input("Enter password:"))
         print("Forget password")
    else:
        print("please enter number between 1 or 2")
        #additional changes
        #1.check for 10 digit no.
        #2.even check for password
def newvoter():
    age=int(input("enter your age:"))
    if age>=18:
        print("you are eligble")
        print("Form 6")
        name=input("Please!enter your name: ")
        print("first name/middle name/surname")
        print("Discalimer:if name not filled in english translated by software")
        #10 digit
        phone=input("please!enter phone no:")
        #8 digit
        DOB=input("please!enter date of birth:")
        #gender(if else)
        gen=print("""select your gender:
                  1.Male
                  2.Female
                  3.other""")
        user=int(input("Please!Enter your gender(1-3): "))
        #12 digit
        print("aadhar card")
        card=int(input("please enter your aadhar card no: "))
        """print("pan card")
        card2=int(input("please enter your pan card no: "))"""
    else:
        print("Invalid")
while True:
    print("""please enter your choice:
          1.login
          2.new voter
          3.exit""")
    user=int(input("Please!Enter your between(1-3):"))
    if user==1:
        login()
    elif user==2:
        newvoter()
    elif user==3:
        break
    else:
        print("please enter valid choice")
        
