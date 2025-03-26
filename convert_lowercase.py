"""
Prog03. lower() converts all characters of the string into lower case. 
Create a program that do the same functionality without using lower() function.
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
    word = input("Enter Word:")

    #This will store the lowercase character
    result = ""

    #convert the word into all lowercase
    for char in word:
        #convert in ascii code
        if 65 <= ord(char) <= 90:
            #add 32 to find its lowercase equevalent
            result += chr(ord(char) + 32) 
        else:
            #print the same if already lowercase or a number
            result += char

    #print the lowercase word
    print(result)
    
    try_again = ask_quit()