"""
Prog05. startswith() check if the string beginning part matches the function parameter. 
Create a program that do the same functionality without using startswith() function.
"""

#ask user to enter a word
word = input("Enter Word: ")
#ask user to input any character
start_charac = input("Enter characters: ")
#initialize boolean value
start_with = True
#check if the the condition is True
if word[:len(start_charac)] == start_charac:
    start_with = True
else:
    start_with = False
#print if true or false
print(start_with)