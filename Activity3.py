#input a word
text = str(input("Enter a word: "))
#Reverse string
#using step value as -1 to itrate in reverse
revtext = text[::-1]
text = revtext
print("Reverse of given string is")
print(text)
