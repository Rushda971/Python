import time

# Base class for all payment types
class PaymentMethod:
    def process_payment(self, name):
        raise NotImplementedError("Subclasses must implement this method.")

# CreditCard with 3 password attempts
class CreditCard(PaymentMethod):
    def process_payment(self, name):
        password = 1245678
        amount_input = input("Enter amount to transfer: ")
        if not amount_input.isdigit():
            print("Invalid amount. Please enter a number.")
            return
        amount = int(amount_input)

        attempts = 3
        while attempts > 0:
            user_input = input("Enter password: ")
            if not user_input.isdigit():
                print("Invalid password. Only numbers allowed.")
                continue

            user_password = int(user_input)
            if user_password == password:
                print(f"{name}, money transfer of {amount} was successful via Credit Card.")
                return
            else:
                attempts -= 1
                print(f"Incorrect password. Attempts left: {attempts}")
        
        print("Transaction failed: Too many incorrect attempts.")

# OnlineBanking with QR timeout logic
class OnlineBanking(PaymentMethod):
    def process_payment(self, name):
        print("""Select payment method:
1. QR Code
2. Phone Number Transfer
3. Bank Account Transfer""")
        option = input("Choose (1-3): ")
        if option == "1":
            print("Displaying QR code. Please scan within 3 seconds...")
            time.sleep(3)
            user = input("Did you scan the QR code? (yes/no): ").strip().lower()
            if user == "yes":
                print("QR code scanned. Payment successful.")
            else:
                print("QR code expired. Payment failed.")
        elif option == "2":
            phone = input("Enter phone number: ")
            print(f"Transfer initiated to phone number {phone}")
        elif option == "3":
            acc = input("Enter bank account number: ")
            print(f"Transfer initiated to account {acc}")
        else:
            print("Invalid option.")

# DebitCard with PIN and attempt limit
class DebitCard(PaymentMethod):
    def process_payment(self, name):
        pin = 4321
        amount_input = input("Enter amount to transfer: ")
        if not amount_input.isdigit():
            print("Invalid amount.")
            return
        amount = int(amount_input)

        attempts = 3
        while attempts > 0:
            pin_input = input("Enter PIN: ")
            if not pin_input.isdigit():
                print("PIN must be numeric.")
                continue

            if int(pin_input) == pin:
                print(f"{name}, money transfer of {amount} was successful via Debit Card.")
                return
            else:
                attempts -= 1
                print(f"Incorrect PIN. Attempts left: {attempts}")

        print("Transaction failed: Too many incorrect attempts.")

# GooglePay implementation
class GooglePay(PaymentMethod):
    def process_payment(self, name):
        upi_id = input("Enter your UPI ID: ")
        amount_input = input("Enter amount to pay via GooglePay: ")
        if not amount_input.isdigit():
            print("Invalid amount.")
            return
        amount = int(amount_input)
        print(f"{name}, payment of {amount} via GooglePay UPI ({upi_id}) successful.")

# Main system controller
class PaymentSystem:
    def __init__(self):
        self.methods = {
            1: CreditCard(),
            2: OnlineBanking(),
            3: DebitCard(),
            4: GooglePay()
        }

    def start(self):
        while True:
            name = input("Enter your name: ").strip()
            print("""\nChoose a payment method:
1. Credit Card
2. Online Banking
3. Debit Card
4. GooglePay
5. Cancel/Quit""")
            choice_input = input("Enter number (1-5): ")

            if not choice_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            choice = int(choice_input)

            if choice in self.methods:
                self.methods[choice].process_payment(name)
            elif choice == 5:
                confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
                if confirm == "yes":
                    print("Exiting payment system.")
                    break
            else:
                print("Invalid option. Please enter a number between 1 and 5.")

# Run the system
if __name__ == "__main__":
    system = PaymentSystem()
    system.start()
