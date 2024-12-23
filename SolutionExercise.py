import os
def cleanFiles(currentMem, exMem):
    # Verifica si el archivo 'currentMem' existe; si no, lo crea vacío
    # if not os.path.exists('currentMem'):
    #     with open('currentMem', 'w') as temp_file:
    #         temp_file.write("Membership No  Date Joined  Active  \n")  # Encabezados iniciales

    with open('members.txt','r+') as writeFile:
        with open('inactive.txt','a+') as appendFile: 
            writeFile.seek(0) 
            members = writeFile.readlines()

            #remove header:
            header = members[0]
            members.pop(0)
            
        inactive = [member for member in members if ('no' in member)]

        writeFile.seek(0)
        writeFile.write(header)

        for member in members:
            if (member in inactive):
                appendFile.write(member)
            else:
                writeFile.write(member)
        writeFile.truncate()

# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = r'F:/DataAnalysisPath/members.txt'
exReg = r'F:/DataAnalysisPath/inactive.txt'
# cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
