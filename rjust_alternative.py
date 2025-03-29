"""
Prog06. rjust() add space characters at the beginning of the string to complete the number
of characters specifies in function parameter. Create a program that do the same 
functionality without using rjust() function.
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

#number validator
def valid_num(msg):
    while True:    
        num = input(msg)
        try:
            return int(num)
        except:
            print("Invalid Number")

try_again = True
while try_again:
    #Ask user to input word/s
    word = input("Enter Words: ")

    #ask user the width 
    width = valid_num("Enter Width: ")

    #print with the in respect with the width
    space = " " * (width - len(word))
    maangas_rjust = space + word
    print(maangas_rjust)
    
    #ask user to quit
    try_again = ask_quit()