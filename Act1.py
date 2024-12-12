# There are various types of objects in python, such as:
# Integers, floats, booleans, str, and so on

x = 11 # Integer 
11.0 # Float
"Hello.py! " # String

# How to know the type of a variable: 

print("The type of the variable 'x' is: " , type(x))

# Casting 

# Convert 2 to a float

float(2)

# Convert integer 2 to a float and check its type

type(float(2))

# Casting 1.1 to integer will result in loss of information

int(1.1)

# Convert a string into an integer with error

# int('1 or 2 people')

# Convert a string into an integer

int('1')

# Convert an integer to a string

str(1)

# Integer division operation expression (Rounds the result)
25 // 6


print(11//2)

# Introduced in Python 3.6, f-strings are a new way to format strings in Python. 
# They are prefixed with 'f' and use curly braces {} to enclose the variables that will be formatted. For example:

name = "John"
age = 30

print(f"My name is {name} and I am {age} years old.")

# This is another way to format strings in Python. It uses curly braces {} as placeholders for variables 
# which are passed as arguments in the format() method. For example:

print("My name is {} and I am {} years old.".format(name, age))

# This is one of the oldest ways to format strings in Python. It uses the % operator to replace variables in the string. For example:

print("My name is %s and I am %d years old." % (name, age))

# F-strings are also able to evaluate expressions inside the curly braces, which can be very handy. For example:

x = 10
y = 20
print(f"The sum of x and y is {x+y}.")

# In Python, raw strings are a powerful tool for handling textual data, especially when dealing with escape characters. 
# By prefixing a string literal with the letter ‘r’, Python treats the string as raw, meaning it interprets backslashes as 
# literal characters rather than escape sequences.

regular_string = "C:\new_folder\file.txt"
print("Regular String:", regular_string)

raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)

name = "Michael Jackson"
# Print the first element in the string

print(name[0])
# Print the last element in the string

print(name[-1])
# Print the first element in the string

print(name[-15])

# We can obtain multiple characters from a string using slicing, we can obtain the 0 to 4th and 8th to the 12th element:

# Take the slice on variable name with only index 0 to index 3

name[0:4]
name[8:12]

# We can also input a stride value as follows, with the '2' indicating that we are selecting every second variable:

# Get every second element. The elments on index 1, 3, 5 ...

name[::2]

# Get every second element in the range from index 0 to index 4

name[0:5:2]

# r will tell python that string will be display as raw string

print(r" Michael Jackson \ is the best" )

# Include back slash in string

print(" Michael Jackson \\ is the best" )

# Convert all the characters in string to upper case

a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# Replace the old substring with the new target substring is the segment has been found in the string

a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
b

# Find the substring in the string. Only the index of the first elment of substring in string will be the output

name = "Michael Jackson"
name.find('el')

# In Python, RegEx (short for Regular Expression) is a tool for matching and handling strings.

import re

# The search() function searches for specified patterns within a string. 
# Here is an example that explains how to use the search() function to search for the word "Jackson" in the string "Michael Jackson is the best".

s1 = "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

# Special Sequence	Meaning	Example
# \d	Matches any digit character (0-9)	"123" matches "\d\d\d"
# \D	Matches any non-digit character	"hello" matches "\D\D\D\D\D"
# \w	Matches any word character (a-z, A-Z, 0-9, and _)	"hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"
# \W	Matches any non-word character	"@#$%" matches "\W\W\W\W"
# \s	Matches any whitespace character (space, tab, newline, etc.)	"hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"
# \S	Matches any non-whitespace character	"hello_world" matches "\S\S\S\S\S\S\S\S\S"
# \b	Matches the boundary between a word character and a non-word character	"cat" matches "\bcat\b" in "The cat sat on the mat"
# \B	Matches any position that is not a word boundary	"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")
# The match.group() method is used in Python's re module to retrieve the part of the string where the regular expression pattern matched. Here's a detailed explanation:

# Purpose
# - Extract Matched Text: match.group() returns the exact substring that matched the pattern.
 
# Usage
# - When you use functions like re.search() or re.match(), they return a match object if the pattern is found. You can then use match.group() to get the matched text.

# Here `match.group()` retrieves the substring 1234567890 from the text, which is the part that matched the pattern.

pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)

# The regular expression pattern is defined as r"\W", which uses the \W special sequence to match any character that is not a word character (a-z, A-Z, 0-9, or _). The string we're searching for matches in is "Hello, world!".

# The findall() function finds all occurrences of a specified pattern within a string.

s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result)

# A regular expression's split() function splits a string into an array of substrings based on a specified pattern.

# Use the split function to split the string by the "\s"
split_array = re.split(r"\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array)

# Here's a detailed explanation:

# re.split("\s", s2):

# re.split: This function splits a string by the occurrences of a pattern.

# r"\s": This is a regular expression pattern that matches any whitespace character (spaces, tabs, newlines, etc.).
# s2: This is the string that you want to split.

# The sub function of a regular expression in Python is used to replace all occurrences of a pattern in a string with a specified replacement.

# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 