# Lists and tuples 
# Are sequences, separated by commas within a pair of parenthesis
# We can concat and slice tuples 
# Tuples are Immutable


#Lists are represented with square brackets

#Lists and tuples can be of more than 1 dimension

L = ["Michael Jackson", 10.2,1982]
L.append(["A",1])
print(L)
# ['Michael Jackson', 10.2, 1982, ['A', 1]]   

# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)

# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)
# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A)

# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)


# Clone (clone by value) the list A

B = A[:]

print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

# Create a list <code>a_list</code>, with the following elements <code>1</code>, <code>hello</code>, <code>\[1,2,3]</code> and <code>True</code>.

L = [ 1, "Hello",[1,2,3], True] 
print(L)

print(L[1])

# Retrieve the elements stored at index 1, 2 and 3 of a_list.
L[1:4]

# Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:

A = [1, 'a']
B = [2, 1, 'd']

C = A + B


#######################################################################################################

#Dictionaries

# A dictionary consists of keys and values. It is helpful to compare a dictionary to a list. Instead of being indexed numerically like a list, dictionaries have keys. 
# These keys are the keys that are used to access values within a dictionary.

# The best example of a dictionary can be accessing person's detais using the social security number.
# Here the social security number which is a unique number will be the key and the details of the people will be the values associated with it.

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict)

# Access to the value by the key

print(Dict["key1"])
# Each key is separated from its value by a colon ":". Commas separate the items, and the whole dictionary is enclosed in curly braces.
# An empty dictionary without any items is written with just two curly braces, like this "{}".

# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print(release_year_dict)

# Get value by keys

release_year_dict['Thriller'] 

# Get all the keys in dictionary

release_year_dict.keys() 

# Get all the values in dictionary

release_year_dict.values() 

######################################
# Sets

# Type of collection
#     You can input different .py types

# Are unordered and only have unique elements: Do not record element position and there is only one of a particular element


# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set


# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
# Add element to set

A.add("NSYNC")
# Remove the element from set

A.remove("NSYNC")
# Verify if the element is in the set

"AC/DC" in A

# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets

print(album_set1)
print(album_set2)

# Find the intersections You can find the intersect of two sets as follow using &:

intersection = album_set1 & album_set2
intersection

# Find the difference in set1 but not set2 You can find all the elements that are only contained in album_set1 using the difference method:

album_set1.difference(album_set2)  

# You can also find the intersection of album_list1 and album_list2, using the intersection method:

# Use intersection method to find the intersection of album_list1 and album_list2

album_set1.intersection(album_set2)   
# Find the union of two sets

album_set1.union(album_set2)

# Check if superset

set(album_set1).issuperset(album_set2) 
# Check if subset

set(album_set2).issubset(album_set1)   