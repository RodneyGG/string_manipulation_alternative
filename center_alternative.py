"""
Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. 
Create a program that do the same functionality without using center() function.
"""

#make a function to ask the user to quit
def ask_quit():
    while True:
        ask_user = input("Do you wish to exit the program? (Y/N)").strip().lower()
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input")

#make a function that center it 
def maangas_na_center(word, width):
    if len(word) >= width:
        return word
    else:
        space = (width - len(word)) // 2
        return " " * space + word + " " * space 
    
#Number VAlidator  
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
    #Ask the user to input a word
    word = input("Enter Word: ")
    #ask the user what is the desired width
    width = valid_num("Enter Width: ")

    #print the word and center it with respect to the width
    centered_word = maangas_na_center(word, width) 
    print(centered_word)
    
    #ask user to quit
    try_again = ask_quit()