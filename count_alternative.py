"""
Prog08. count() return how many time the function parameter appear in the string. 
Create a program that do the same functionality without using count() function.
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
    #ask user to input a text
    text = input("Enter Text: ")
    #ask user to input character or word it like to count
    parameter = input("What character or word would you like to count?\n")

    #initialize variables
    count = 0
    text_length = len(text)
    param_length = len(parameter)

    #counter
    for i in range(text_length - param_length + 1):
        if text[i:i+len(parameter)] == parameter:
            count += 1 
            
    #print the count
    print(count)
    
    try_again = ask_quit()