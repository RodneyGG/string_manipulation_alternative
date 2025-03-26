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

def ask_quit():
    while True:
        ask_user = input("Do you wish to exit the program? (Y/N)").strip().lower()
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input")

try_again = True
while try_again:
    #Ask the user to input name with leading spaces
    name = count_space("Enter Name: ")

    #print name without spaces
    print(name)
    
    try_again = ask_quit()
