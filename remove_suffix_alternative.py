"""
Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. 
Create a program that do the same functionality without using removesuffix() function.
"""

#make a function ask the user to quit
def ask_quit():
    while True:
        ask_user = input("Do you wish to exit the program? (Y/N)").lower().strip()
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input")

try_again = True
while try_again:
    #ask the user to input a word
    word = input("Enter Word: ")

    #ask the user to input a suffix
    suffix = input("Enter Suffix: ")

    #remove the suffix
    if word[-len(suffix):] == suffix:
        word = word[:-len(suffix)]

    #print the word without suffix
    print(word)
    
    #ask the user to quit 
    try_again = ask_quit()