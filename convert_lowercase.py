"""
Prog03. lower() converts all characters of the string into lower case. 
Create a program that do the same functionality without using lower() function.
"""

#ask the user to input a word
word = input("Enter Word:")
#convert the word into all lowercase
result = ""
for char in word:
    #convert in ascii code
    if 65 <= ord(char) <= 90:
        #add 32 to find its lowercase equevalent
        result += chr(ord(char) + 32) 
    else:
        #print the same if already lowercase or a number
        result += char
#print the lowercase word
print(result)