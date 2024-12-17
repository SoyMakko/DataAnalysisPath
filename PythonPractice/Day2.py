# Input and Variables

name = input("Write your name: ")

age = input("Age: ")

print(f"Your name is {name} and your age is {age}!") # f string in python

print(" \n Form 2 of printing: Your name is {} and your age is {}!".format(name,age)) 

# EXERCISE!

name = input("What's your name?\n")
food = input("What's your favourite food?\n")
music = input("What's your favourite music?\n")
home = input("Where do you live?\n")


print(f"""
      You are: {name}
      Your favourite food is {food}, tasty!
      Your favourite music is {music} and you live in {home}!
      Glad to get to know you mate! """)
