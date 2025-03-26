"""
Prog01. lstrip() remove the space characters at the beginning of the string. 
Create a program that do the same functionality without using lstrip() function.
"""

#Count the spaces
def count_space(msg):
    name = input(msg)
    #Identify how long is the leading spaces
    space = 0
    while space < len(name) and name[space] == " ":
        space += 1
    #maangas
    return name[space:]


#Ask the user to input name with leading spaces
name = count_space("Enter Name: ")

#print name without spaces
print(name)
