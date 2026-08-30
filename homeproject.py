import random
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

password = "" 
for i in range (4):
    password = password + random.choice(lowercase)
    password = password + random.choice(uppercase)
    password = password + random.choice(numbers)

password = list(password)
random.shuffle(password)

password = "".join(password)
print("your random password is: ", password)
    
