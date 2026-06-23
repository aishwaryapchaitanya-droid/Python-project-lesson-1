x = input("Enter a character: ")
ASCII_Value = ord(x)
print("The ASCII vaue of", x, "is", ASCII_Value) 
if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefjhijklmnopqrstuvwxyz":
    print("Alphabet")

elif x in "1234567890":
    print("Digit")

else:
    print("Special character")