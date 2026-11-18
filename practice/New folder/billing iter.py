#iteration
#billing at a grocery store(list iteration)
"""class grocery:
    def __init__(self,item):
        self.item=item
    def display(self):
        pass
item=[10,60,70,67,45,37,68]
order=iter(item)
for x in item:
    print(x)
print("total grocery:",sum(item))
x=grocery(item)
x.display()
#sending email to customer
class email:
    def __init__(self,customers):
        self.customer=customers
    def display(self):
        pass
customers=["eshika","zohra","sejal","liza","faiza"]
msg=(f"{customers}hey,rushda is learning python")

for x in msg:
    
   print(x)
x=email(customers)
x.display()"""
#playing song from playlistclass Email:
class email:
    def __init__(self, customers):
        self.customers = customers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.customers):
            msg = f"{self.customers[self.index]} hey, Rushda is learning Python!"
            self.index += 1
            return msg
        else:
            raise StopIteration

customers = ["Eshika", "Zohra", "Sejal", "Liza", "Faiza"]
myclass = email(customers)

for message in myclass:
    print(message)
