"""
Prog09. index() return the first location of the function parameter in the string. 
Create a program that do the same functionality without using index() function.
"""

#ask the user to input a text
text = input("Enter text: ")

#ask the user to input tha character they want to find
parameter = input("What character or word would you like to find?\n")

#initialize values
position = -1
text_length = len(text)
param_length = len(parameter)

#find the first time the character was found
for i in range(text_length - param_length + 1):
    if text[i:i+param_length] == parameter:
        position = i
        break

#print the number
if position == -1:
    print(f"There is no {parameter} in {text}")
else:
    print(position)
