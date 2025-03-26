"""
Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. 
Create a program that do the same functionality without using ljust() function.
"""

#make a function that ask the user to quit
def ask_quit():
    while True:
        ask_user = input("Do you wish to exit the program? (Y/N)").strip().lower()
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input")


#make a function that add the justify
def make_space(word, desired_adjust):
    if len(word) < desired_adjust:
        return word + " " * (desired_adjust - len(word))
    else:
        return word

#added a function so that when user enter letter it will not break    
def valid_num(msg):
    while True:
        num = input(msg)
        try:
            return int(num)
        except:
            print("Only type numbers")
            continue

try_again = True
while try_again:
    #Ask the user to enter a word
    word = input("Enter Word: ")
    #ASk the user what is the desired adjust
    desired_adjust = valid_num("Enter desired adjust: ")

    #print word with the desired adjust
    left_justify = make_space(word, desired_adjust) 
    print(left_justify)
    
    #ask the user to quit
    try_again = ask_quit()
    
