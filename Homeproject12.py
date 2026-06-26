n = int(input("Enter a decimal number: "))
binary = " "
while n>0:
  remainder = n%2
  binary = binary+ str(remainder)
  n = n//2
binary = binary[::-1]
print("Binary number = ",binary)
