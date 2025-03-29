"""
Prog03. upper() converts all characters of the string into upper case. 
Create a program that do the same functionality without using upper() function.
"""

#ask the user to input word
word = input("Enter Word: ")

#concatenate characters here
result = ""

#convert to upper case using ascii
for charac in word:
    if 97 <= ord(charac) <= 122:
        result += chr(ord(charac) - 32)
    else:
        result += charac

#print all uppercase
print(result)