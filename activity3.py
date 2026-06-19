print("Select your ride: ")
print("1. Two wheeler ")
print("2. Four wheeler ")

choice = int (input("Enter your choice: "))

if (choice == 1):
    print("What type of two wheeler? ")
    print("1. Scooty\n")
    print("2. Scooter\n")

    choice2 = int(input("Enter your choice 2: "))
    if choice2==1:
        print("You have seleted scooty")
    
    else:
        print("You have selected scooter")

elif(choice == 2):
    print(("What type of four wheeler? "))
    print("1.Sedan")
    print("2.XUV")
    choice3 = int(input("enter your choice 3: "))

    if choice3 ==1:
        print("You have selected sedan")
    else: 
        print("you have slected XUV")

else:
    print("wrong choice")









