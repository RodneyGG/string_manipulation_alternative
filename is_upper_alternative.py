"""
Prog04. isupper() check if all characters of the string is on upper case. 
Create a program that do the same functionality without using isupper() function.
"""

#make a function identify if the string is on uppercase
def check_upper(msg):
    word = input(msg)
    for charac in word:
        if 97 <= ord(charac) <= 122:
            return False
        else:
            return True

#ask the user to input a word 
word = check_upper("Enter Word: ")
    
#print true if uppercase else false
print("Uppercase:",word)