"""
Prog04. isupper() check if all characters of the string is on upper case. 
Create a program that do the same functionality without using isupper() function.
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

#make a function identify if the string is on uppercase
def check_upper(msg):
    word = input(msg)
    for charac in word:
        if 97 <= ord(charac) <= 122:
            return False
    return True

try_again = True
while try_again:
    #ask the user to input a word 
    word = check_upper("Enter Word: ")
        
    #print true if uppercase else false
    print("Uppercase:",word)
    
    try_again = ask_quit()