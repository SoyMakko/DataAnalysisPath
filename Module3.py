# elif statement
age = 20

if age >= 21:
    print("You can enter the bar.")
elif age >= 18:
    print("You can watch a movie.")
else:
    print("Sorry, you cannot do either.")

################### Loops

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for color in colors:
    print(color)

# Range function
# If given one argument (e.g., range(11)), it generates a sequence starting from 0 up to (but not including) the given number.

for number in range(11):
    print(number)

# If given two arguments (e.g., range(1, 11)), it generates a sequence starting from the first argument up to (but not including) the second argument.

for number in range(1,11):
    print(number)

# Enumerated: It is used to keep track of both an item and its position in a list

fruits = ["apple", "banana", "orange"] 
vowels = ['a','e','i','o','u']

for index, fruit in enumerate(fruits): 
    if(fruit[0] in vowels):
        print(f"At position {index}, I found an {fruit}")
    else:
        print(f"At position {index}, I found a {fruit}")
for i, x in enumerate(['A', 'B', 'C']):
    print(i, x)

################################### Functions

def add1 (a):
    """
        This is a documentation string: add 1 to a
    """
    b = a + 1
    return b

help(add1)

# We can have global or local variables within a Python project, but when in a function you add the "global" word before some variable it will become global and not local

print(len(['A','B',1]))

print( len([sum([1,1,1])]))

L=[1,3,2]

print(sorted(L))

def print_function(A):
    for a in A:
        print(a + '1')
print_function(['a', 'b', 'c'])

######################################### Exception Handling

# Try and Except : You can use the try and except blocks to prevent your program from crashing due to exceptions

# It can also be used:

# Try... Except... Except 
# Try... Except... Else 
# Try... Except...Finally

# potential code before try catch

# try:
#     # code to try to execute
# except:
#     # code to execute if there is an exception
    
# code that will still execute if there is an exception

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
        

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")


####################### Objects and classes

# Class attributes (class_attribute = value)

# Class attributes are variables shared among all class instances (objects).
# They are defined within the class but outside of any methods.

# class ClassName:
#     # Class attributes (shared by all instances)
#     class_attribute = value

# Constructor method (def init(self, attribute1, attribute2, …):)

# The __init__ method is a special method known as the constructor.It initializes the instance attributes (also called instance variables) when an object is created.

# The self parameter is the first parameter of the constructor, referring to the instance being created.
# attribute1, attribute2, and so on are parameters passed to the constructor when creating an object.
# Inside the constructor, self.attribute1, self.attribute2, and so on are used to assign values to instance attributes.


# class ClassName:
#     # Class attributes (shared by all instances)
#     class_attribute = value
#     # Constructor method (initialize instance attributes)
#     def __init__(self, attribute1, attribute2, ...):
#         pass
#         # ...

class Car:
    # Class attribute (shared by all instances)
    max_speed = 120  # Maximum speed in km/h

    # Constructor method (initialize instance attributes)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0

    # Method for accelerating the car
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed

    # Method to get the current speed of the car
    def get_speed(self):
        return self.speed
    
# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

# Accelerate the cars
car1.accelerate(30)
car2.accelerate(20)

# Print the current speeds of the cars
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")

import matplotlib.pyplot as plt

class Circle (object):
    def __init__(self,radius,color):
        self.color = color
        self.radius = radius
        
    def addRadius(self,r):
        self.radius = self.radius + r
        return(self.radius)
    
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

    
class Rectangle (object):
    def __init__(self,color,height,width):
        self.color = color
        self.height = height
        self.width = width
    
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
    
RedCircle = Circle(10, 'red')
RedCircle.drawCircle()       
        
# Use method to change the object attribute radius

print('Radius of object:',RedCircle.radius)
RedCircle.addRadius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.addRadius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)


SkinnyBlueRectangle = Rectangle( 'blue',2, 3)
SkinnyBlueRectangle.drawRectangle()