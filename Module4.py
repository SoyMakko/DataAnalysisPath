## Reading text files 

file = open('file.txt','r')
content = file.read()
# print(content)
file.close()

file = open('file.txt','a')
content = file.write("\n text added")
# print(content)
file.close()

# with statement

with open('file.txt','r') as file:
    content = file.read()
    # print(content)

    line1 = file.readline()  # Reads the first line 
    line2 = file.readline()  # Reads the second line
    print(line1)

# The file automatically closes when using this sentence
with open('file.txt','r') as file:
    while True: 
        line = file.readline() 
        if not line: 
                break  # Stop when there are no more lines to read 
        print(line)


file = open('file.txt','r')
# Navigate to the Desired Position (Optional):
file.seek(10)
# Read specific characters
characters = file.read(5)  # Read the next 5 characters
# was c because we started in the 10th position with seek
print(characters)
file.close()


## Writing files  is just change the mode from r to w and use file.write


with open('file.txt','r') as readfile:
    with open('CopiedFile.txt','w') as writefile:
        for line in readfile:
            writefile.write(line)
        print("The text was succesfully copied!")

# ‘r’	'r'	    Read mode. Opens an existing file for reading. Raises an error if the file doesn't exist.
# ‘w’	'w' 	Write mode. Creates a new file for writing. Overwrites the file if it already exists.
# ‘a’	'a'	    Append mode. Opens a file for appending data. Creates the file if it doesn't exist.
# ‘x’	'x'	    Exclusive creation mode. Creates a new file for writing but raises an error if the file already exists.
# ‘rb’	'rb'	Read binary mode. Opens an existing binary file for reading.
# ‘wb’	'wb'	Write binary mode. Creates a new binary file for writing.
# ‘ab’	'ab'	Append binary mode. Opens a binary file for appending data.
# ‘xb’	'xb'	Exclusive binary creation mode. Creates a new binary file for writing but raises an error if it already exists.
# ‘rt’	'rt'	Read text mode. Opens an existing text file for reading. (Default for text files)
# ‘wt’	'wt'	Write text mode. Creates a new text file for writing. (Default for text files)
# ‘at’	'at'	Append text mode. Opens a text file for appending data. (Default for text files)
# ‘xt’	'xt'	Exclusive text creation mode. Creates a new text file for writing but raises an error if it already exists.
# ‘r+’	'r+'	Read and write mode. Opens an existing file for both reading and writing.
# ‘w+’	'w+'	Write and read mode. Creates a new file for reading and writing. Overwrites the file if it already exists.
# ‘a+’	'a+'	Append and read mode. Opens a file for both appending and reading. Creates the file if it doesn't exist.
# ‘x+’	'x+'	Exclusive creation and read/write mode. Creates a new file for reading and writing but raises an error if it already exists.

# Opening the file in w is akin to opening the .txt file, moving your cursor to the beginning of the text file, writing new text and deleting everything that follows.
#  Whereas opening the file in a is similiar to opening the .txt file, moving your cursor to the very end and then adding the new pieces of text.
# It is often very useful to know where the 'cursor' is in a file and be able to control it. The following methods allow us to do precisely this -

# .tell() - returns the current position in bytes
# .seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to beginning, relative to current
#  position and end

with open('/Example1.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )

    with open('F:\DataAnalysisPath/Example1.txt', 'r+') as testwritefile:
        testwritefile.seek(0,0) #write at beginning of file
        testwritefile.write("Line 1" + "\n")
        testwritefile.write("Line 2" + "\n")
        testwritefile.write("Line 3" + "\n")
        testwritefile.write("Line 4" + "\n")
        testwritefile.write("finished\n")
        #Uncomment the line below
        testwritefile.truncate()
        testwritefile.seek(0,0)
        print(testwritefile.read())