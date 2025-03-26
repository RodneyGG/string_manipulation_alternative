"""
Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. 
Create a program that do the same functionality without using title() function.
"""

#ask user to quit
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
    #Ask the user to enter word/s
    sentence = input("Enter Word/s: ") 
    #Split the word
    words = sentence.split()

    #the first letter for each word must be Uppercase and the rest is lowercase
    title_case = []
    for word in words:
        title_case.append(word[0].upper() + word[1:].lower())

    #print the word 
    for word in title_case:
        print(word, end=" ")
        
    #ask the user to quit
    print("")
    try_again = ask_quit()