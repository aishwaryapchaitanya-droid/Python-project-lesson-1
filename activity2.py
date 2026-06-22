#INput a word or a sentence
string = input("PLease enter your own string: ")

string2 = ('')
#loop for printing in reverse
for i in string:
    string2 = i+string2

print("\n the original string = ", string)
print("\nThe reversed string = ", string2)