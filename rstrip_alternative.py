"""
Prog01. rstrip() remove the space characters at the end of the string. 
Create a program that do the same functionality without using rstrip() function.
"""

#Ask user to input a word/s
word = input("Enter Word/s: ")

#reverse the word for easier work to count spaces
reversed_word = word[::-1]

#count the spaces
space = 0
while space < len(reversed_word) and reversed_word[space] is " ":
    space += 1
#remove the spaces
no_space = reversed_word[space:]

#reverse the word
word_rstrip = no_space[::-1]  
#print the word without trailing spaces
print(word_rstrip)