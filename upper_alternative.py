"""
Prog03. upper() converts all characters of the string into upper case. 
Create a program that do the same functionality without using upper() function.
"""

#function to ask user to quit
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
    
    #ask user to quit
    try_again = ask_quit()