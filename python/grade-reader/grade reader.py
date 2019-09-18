import os

print('''The file this program is reading must be in the same folder as this program''')

filename = str(input("What is the name of your file? ex: grades.txt >>> "))

inputfile = open(filename, "r")

lines = inputfile.readlines()

length = int(lines[0])

i = 0
while i < length:
    x = int(lines[i])
    if x < 70:
        print("FAIL")
    if x >= 70:
        print("PASS")
    i += 1




    
