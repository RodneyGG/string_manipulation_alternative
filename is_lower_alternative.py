"""
Prog04. islower() check if all characters of the string is on lower case. 
Create a program that do the same functionality without using islower() function.
"""

#ask user to input a word
word = input("Enter Word: ")

#initialize as boolean Value
lower_case = True

#check if the all of the characters are in lowercase using ascii
for charac in word:
    if 65 <= ord(charac)>= 90:
        lower_case = False
        break
    
#print True or False
print(lower_case)