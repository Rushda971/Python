#stack
#CREATING EMPTY LIST FOR STACK
l=[]
#
while True:
    user=int(input("""1.push element
                      2.pop element
                      3.peek element
                      4.display element
                      5.exit"""))
    if user==1:
        n=input("enter the value: ")
        l.append(n)
        #listname.append(valueenter)
        print(l)
    elif user==2:
        if len(l)==0:
            print("empty stack")
        else:
            #remove and return top item
            p=l.pop()
            #remove item
            print(p)
            #update stack
            print(l)
