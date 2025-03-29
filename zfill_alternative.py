"""
Prog07. zfill() add zero characters at the beginning of the string to complete 
the number of characters specifies in function parameter. 
Create a program that do the same functionality without using zfill() function.
"""

#number validator
def valid_num(msg):
    while True:    
        num = input(msg)
        try:
            return int(num)
        except:
            print("Invalid Number.(Whole Number)")

#ask user to input words or numbers
characters = input("Enter Words or Number: ")
#ask user to input a parameter
parameter = valid_num("Enter parameter: ")
#print words or number with leading 0
if len(characters) >= parameter:
    print(characters)
else:
    result = ""
    zero = "0" * (parameter - len(characters))
    result += (zero + characters)
    print(result)
