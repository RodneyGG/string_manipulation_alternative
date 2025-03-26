"""
Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. 
Create a program that do the same functionality without using removeprefix() function.
"""

#Ask the user to input a word
word = input("Enter Word: ")
#Ask for prefix
prefix = input("Enter Prefix: ")

#It will remove prefix it if matches the word
if word[:len(prefix)] == prefix:
    #remove the prefix
    word = word[len(prefix):]
    
#print the word with out prefix
print(word)