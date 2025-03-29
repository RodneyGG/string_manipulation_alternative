"""
Prog06. rjust() add space characters at the beginning of the string to complete the number
of characters specifies in function parameter. Create a program that do the same 
functionality without using rjust() function.
"""

def valid_num(msg):
    while True:    
        num = input(msg)
        try:
            return int(num)
        except:
            print("Invalid Number")

#Ask user to input word/s
word = input("Enter Words: ")

#ask user the width 
width = valid_num("Enter Width: ")

#print with the in respect with the width
space = " " * (width - len(word))
maangas_rjust = space + word
print(maangas_rjust)