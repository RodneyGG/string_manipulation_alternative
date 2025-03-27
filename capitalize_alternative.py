"""
Prog09. capitalize() makes the first letter of the string, capital letter. 
And all other letter in small case. Create a program that do the same functionality 
without using capitalize() function.
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
    #Ask the user to enter a sentence
    text = input("Enter a sentence: ")

    if text:
        #Make the first character of the text capitalize
        capitalize_text = text[0].upper() + text[1:].lower()
    else:
        capitalize_text = ""
        
    #print the Capitalize verision
    print(capitalize_text)
    
    #ask user to quit the program
    try_again = ask_quit()