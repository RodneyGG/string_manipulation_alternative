"""
Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. 
Create a program that do the same functionality without using title() function.
"""

#Ask the user to enter word/s
sentence = input("Enter Word/s: ") 
#Split the word
words = sentence.split()

#the first letter for each word must be Uppercase and the rest is lowercase
title_case = []
for word in words:
    title_case.append(word[0].upper() + word[1:].lower())

#print the word 
for word in title_case:
    print(word, end=" ")