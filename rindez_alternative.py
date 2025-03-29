"""
Prog10. rindex() return the first location of the function parameter in the string 
starting from the last character. Create a program that do the same functionality 
without using rindex() function.
"""

#ask user to input a text 
text = input("Enter text: ")

#ask user to input any character it wnt t find
parameter = input("What character or word would you like to find?\n")

#initialize values
position = -1
text_length = len(text)
param_length = len(parameter)

#find the charectes starting from the right
for i in range(text_length - 1, -1, -1):
    if text[i:i+param_length] == parameter:
        position = i
        break 
    
#print the postion
if position == -1:
    print("Character not in the string")
else:
    print(position)