"""
Prog09. capitalize() makes the first letter of the string, capital letter. 
And all other letter in small case. Create a program that do the same functionality 
without using capitalize() function.
"""

#Ask the user to enter a sentence
text = input("Enter a sentence: ")
#Make the first character of the text capitalize
capitalize_text = text[0].upper() + text[1:].lower()
#print the Capitalize verision
print(capitalize_text)