"""
Prog04. islower() check if all characters of the string is on lower case. 
Create a program that do the same functionality without using islower() function.
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
    #ask user to input a word
    word = input("Enter Word: ")

    #initialize as boolean Value
    lower_case = True

    #check if the all of the characters are in lowercase using ascii
    for charac in word:
        if 65 <= ord(charac)>= 90:
            lower_case = False
            break
        
    #print True or False
    print(lower_case)
    
    #ask user to exit the program
    try_again = ask_quit()