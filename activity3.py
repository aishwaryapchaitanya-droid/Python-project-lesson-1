#take input from user
num = int(input("Enter a number: "))
#store original number
original = sum 
#initialize sum
total = 0 
#find dum of cubes of digits
while num>0:
    digit = num % 10  #get last digit
    total = total + digit**3#add cube of digit
    num = num//10 #remove last digit
#check armstrong number
if original == total: 
    print("is is an Armstrong number", original)
else: 
    print("is is not an Armstrong number", original)
