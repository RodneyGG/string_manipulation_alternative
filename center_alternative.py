"""
Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. 
Create a program that do the same functionality without using center() function.
"""

#make a function that center it 
def maangas_na_center(word, width):
    if len(word) >= width:
        return word
    else:
        space = (width - len(word)) // 2
        return " " * space + word + " " * space 
    
#Number VAlidator  
def valid_num(msg):
    while True:
        num = input(msg)
        try:
            return int(num)
        except:
            print("Only type numbers")
            continue
        
#Ask the user to input a word
word = input("Enter Word: ")
#ask the user what is the desired width
width = valid_num("Enter Width")

#print the word and center it with respect to the width
centered_word = maangas_na_center(word, width) 
print(centered_word)