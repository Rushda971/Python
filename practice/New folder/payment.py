#polymorphism:payment system
"""1. Payment System
Scenario: A company supports multiple payment methods: CreditCard, PayPal, and BankTransfer.
All have a process_payment() method but with different logic.
Task: Add a new payment method, say GooglePay, and integrate it without changing existing loop logic.
"""
class payment:
    def __init__(self):
        pass
    def paymentmethod(self):
        while:
            self.name=input("enter your name: ")
            print("""1.credit card
                  2.online banking(net banking)
                  3.debit card
                  4.cancel or quit
                  """)
            print("select payment method")
            user=int(input("enter number(1-3): "))
            if user==1:

            elif user==2:

            elif user==3:

            elif user==4:
                print("sure you want to exit?")
                cancel=input("enter yes or no: ")
                if user=="yes":
                    break
                else user=="no":
                    continue
            else:
                print("please enter valid number between (1-4)")
class creditcard:
    def __init__(self):
        password=1245678
        money=int(input("please enter amount to transfer: "))
        userpassword=int(input("please enter password: "))
        if password==userpassword:
            print(f"{self.name},money transfer {money} successfully")
        else:
            for x in userpassword:
                
            print("incorrect password")
class onlinebanking(creaditcard):
    def __init__(self):
        super().__init__(self)
        user=print("""select payment method:
                   1.QR code
                   2.phone number transfer
                   3.bank account tranfer""")
        user(int(input("select number (1-4): ")))
        if user==1:
            print("QR code")
            print("here is your qr code")
            print("valid for next 2 mins")
        elif user==2:
            print("phone number transfer")
            phone=int(input("enter phone number: "))
            print
            
        
    
class debitcard:
    
    
