"""
Prog07. zfill() add zero characters at the beginning of the string to complete 
the number of characters specifies in function parameter. 
Create a program that do the same functionality without using zfill() function.
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
            print("Invalid Number.(Whole Number)")

try_again = True
while try_again:
    #ask user to input words or numbers
    characters = input("Enter Words or Number: ")
    #ask user to input a parameter
    parameter = valid_num("Enter parameter: ")

    #print words or number with leading 0
    if len(characters) >= parameter:
        print(characters)
    else:
        result = ""
        zero = "0" * (parameter - len(characters))
        result += (zero + characters)
        print(result)

    #ask user to quit
    try_again = ask_quit()