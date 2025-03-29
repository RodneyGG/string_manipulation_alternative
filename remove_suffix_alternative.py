"""
Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. 
Create a program that do the same functionality without using removesuffix() function.
"""

#ask the user to input a word
word = input("Enter Word: ")

#ask the user to input a suffix
suffix = input("Enter Suffix: ")

#remove the suffix
if word[-len(suffix):] == suffix:
    word = word[:-len(suffix)]

#print the word without suffix
print(word)