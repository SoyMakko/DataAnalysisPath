from colorama import Fore, Style, init
#When working locally
import urllib.request
init(autoreset = True)
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

print(f"El archivo se ha descargado como '{filename}'.")
example1 = "example1.txt"
file1 = open(example1,'r')
print(f"Name of the file: \t {Fore.RED} {file1.name}")
print(f"The mode the file object is in: \t {Fore.RED} {file1.mode}")

fileContent = file1.read()
print(fileContent)
file1.close()

# Better way to open a file:

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent) 
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars

# Iterate through the lines

with open(example1,"r") as file1:
        i = 0
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
            
# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()

#Not locally 

# # Download Example file
# !wget Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt

# from pyodide.http import pyfetch

# import pandas as pd

# filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"

# async def download(url, filename):

#     response = await pyfetch(url)

#     if response.status == 200:

#         with open(filename, "wb") as f:

#             f.write(await response.bytes())

# await download(filename, "example1.txt")

# print("done")

