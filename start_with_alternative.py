"""
Prog05. startswith() check if the string beginning part matches the function parameter. 
Create a program that do the same functionality without using startswith() function.
"""
#make a function that ask user to quit
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
    #ask user to enter a word
    word = input("Enter Word: ")

    #ask user to input any character
    start_charac = input("Enter characters: ")

    #initialize boolean value
    start_with = True

    #check if the the condition is True
    if word[:len(start_charac)] == start_charac:
        start_with = True
    else:
        start_with = False

    #print if true or false
    print(start_with)
    
    #ask user to quit
    try_again = ask_quit()