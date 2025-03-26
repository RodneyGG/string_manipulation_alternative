"""
Prog05. endswith() check if the string end part matches the function parameter. 
Create a program that do the same functionality without using endswith() function.
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
    #ask the user to input a word
    word = input("Enter Word: ")
    ending_word = input("Enter the ending word: ")
    #identify if the word end with the chosen word
    ends_with = True
    if word[-len(ending_word):] == ending_word:
        ends_with = True
    else:
        ends_with = False
    #print true or false
    print(ends_with)
    
    try_again = ask_quit()