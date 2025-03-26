"""
Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. 
Create a program that do the same functionality without using removeprefix() function.
"""
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
    #Ask the user to input a word
    word = input("Enter Word: ")
    #Ask for prefix
    prefix = input("Enter Prefix: ")

    #It will remove prefix it if matches the word
    if word[:len(prefix)] == prefix:
        #remove the prefix
        word = word[len(prefix):]
        
    #print the word with out prefix
    print(word)
    
    try_again = ask_quit()