"""
Prog06. rjust() add space characters at the beginning of the string to complete the number
of characters specifies in function parameter. Create a program that do the same 
functionality without using rjust() function.
"""

#Ask user to input word/s
word = input("Enter Words: ")

#ask user the width 
width = int(input("Enter Width: "))

#print with the in respect with the width
space = " " * (width - len(word))
maangas_rjust = space + word
print(maangas_rjust)