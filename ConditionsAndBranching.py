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