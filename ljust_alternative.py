"""
Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. 
Create a program that do the same functionality without using ljust() function.
"""

#make a function that add the justify
def make_space(word, desired_adjust):
    if len(word) < desired_adjust:
        return word + " " * (desired_adjust - len(word))
    else:
        return word
    

#Ask the user to enter a word
word = input("Enter Word: ")
#ASk the user what is the desired adjust
desired_adjust = int(input("Enter desired adjust: "))

#print word with the desired adjust
print(make_space(word, desired_adjust))