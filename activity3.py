print("Enter marks obtained in 5 subjects")

markone = int(input("Maths: "))
marktwo = int(input("Science: "))
markthree = int(input("Social Studies: "))
markfour = int(input("English: "))
markfive = int(input("French: "))

total = markone + marktwo + markthree + markfour + markfive 
avg = int(total / 5)    
validrange = range(0,101)

if avg not in validrange:
    print("Invalid input!")

elif avg in range (91,101):
    print("Your grade is A1")

elif avg in range (81,91):
    print("your grade is A2")

elif avg in range (71,81):
    print("your grade is B1")

elif avg in range (61,71):
    print("your grade is B2")

elif avg in range(51,61):
    print("your grade is c1")

elif avg in range(41,51):
    print("your garde is C2")

elif avg in range(33,41):
    print("your grade is D")

elif avg in range(21,33):
    print("your garde is E1")

elif avg in range(11,21):
    print("your grade is E2")

else:
    print("Fail")
