"""
Prog01. lstrip() remove the space characters at the beginning of the string. 
Create a program that do the same functionality without using lstrip() function.
"""

#Ask the user to input name with leading spaces
name = input("Enter Name: ")
#Identify how long is the leading spaces
space = 0
while space < len(name) and name[space] == " ":
    space += 1
#print name without spaces
print(name[space:])
