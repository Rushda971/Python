#polymorphism
class area:
    def __init__(num,length,width):
        num.length=int(input("enter length:"))
        num.width=int(input("enter width:"))
        
    def __str__(num):
        return f"num.length,num.width"

    def display(num):
        pass
        
class rectangle(area):
    def __init__(num,length,width):
        area.__init__(num,length,width)
        rectangle=num.length*num.width
        print("rectangle:",rectangle)
        
class parollogram(area):
    def __init__(num,base,height):
        area.__init__(num,base,height)
        num.height=int(input("Parollogram:enter the height: "))
        num.base=int(input("enter the base: "))
        parollogram=num.base*num.height
        print("parollogram:",parollogram)
        
y=rectangle("length","width")
z=parollogram("base","height")

for x in (y,z):
    print(x.length)
    print(x.width)    
"""Constructor Parameters vs. User Input
You passed "length" and "width" as strings to the constructor:

python
Copy
Edit
y = rectangle("length", "width")
But inside __init__, you’re using input() to get user input anyway. This is a mismatch.

Correct Concept:
Either pass real values as arguments or take input inside the constructor — not both.

🔹 2. Polymorphism Not Properly Applied
You defined a base class area with an empty display() method, but you didn't override it in the subclasses.

Correct Concept:
In polymorphism, a base class defines a method, and each subclass provides its own implementation.

python
Copy
Edit
def display(self):
    print("Rectangle area:", self.area)
Then use:

python
Copy
Edit
for shape in shapes:
    shape.display()  # Calls the correct version automatically
🔹 3. Misuse of Class Names as Variables
python
Copy
Edit
rectangle = num.length * num.width
You used rectangle as a variable name inside the rectangle class — this overwrites the class name, which is a dangerous and confusing practice.

Correct Concept:
Avoid naming variables the same as class names.

🔹 4. Improper Use of __str__
Your original __str__ returned:

python
Copy
Edit
return f"num.length,num.width"
This returns the string literal "num.length,num.width" instead of actual values.

Correct Concept:
Use:

python
Copy
Edit
return f"{self.length}, {self.width}"
To output the actual values.

🔹 5. Inheritance without super()
You called the base constructor manually:

python
Copy
Edit
area.__init__(num, length, width)
While it works, the Pythonic way is:

python
Copy
Edit
super().__init__()
It ensures that the parent class is initialized properly, especially in multiple inheritance scenarios.

✅ Concepts You Need to Revisit:
Concept	What You Missed
Polymorphism	Overriding base methods and using a common interface (display() in this case).
Inheritance	Proper use of super() to initialize the parent class.
Constructor design	Avoid mixing input() with passed arguments unless necessary.
Naming conventions	Don’t reuse class names as variable names.
Magic Methods (__str__)	Return real values, not literal strings. """
# Polymorphism example with proper class design

class Area:
    def __init__(self):
        self.length = int(input("Enter length: "))
        self.width = int(input("Enter width: "))

    def display(self):
        pass  # Placeholder for polymorphic behavior


class Rectangle(Area):
    def __init__(self):
        super().__init__()
        self.area = self.length * self.width

    def display(self):
        print(f"Rectangle area: {self.area}")


class Parallelogram(Area):
    def __init__(self):
        self.base = int(input("Parallelogram - Enter the base: "))
        self.height = int(input("Parallelogram - Enter the height: "))
        self.area = self.base * self.height

    def display(self):
        print(f"Parallelogram area: {self.area}")


# Using polymorphism
shapes = [Rectangle(), Parallelogram()]

for shape in shapes:
    shape.display()

class Area:
    def __init__(self):
        pass

    def get_area(self):
        pass

    def display(self):
        print(f"Area: {self.get_area()}")


class Rectangle(Area):
    def __init__(self):
        self.length = int(input("Enter rectangle length: "))
        self.width = int(input("Enter rectangle width: "))

    def get_area(self):
        return self.length * self.width


class Parallelogram(Area):
    def __init__(self):
        self.base = int(input("Enter parallelogram base: "))
        self.height = int(input("Enter parallelogram height: "))

    def get_area(self):
        return self.base * self.height


shapes = [Rectangle(), Parallelogram()]

for shape in shapes:
    shape.display()

    
