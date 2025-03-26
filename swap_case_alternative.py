"""
Prog08. swapcase() reverse the casing of each of the character of the string. 
Create a program that do the same functionality without using swapcase() function.
"""

#FUnction that ask the user to quit
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
    #Ask the user to input a word/s
    word = input("Enter Word: ")

    #make a variable to store the result
    result = ""

    #check if the word is upper or lower and convert it to the other form
    for charac in word:
        if charac.isupper():
            result += charac.lower()
        elif charac.islower():
            result += charac.upper()
        else:
            result += charac

    #print the result
    print(result)
    
    #ask the user to quit
    try_again = ask_quit()