pin = 1234
balance = 5000

user_pin = int(input("Enter your 4 digit pin: "))
if user_pin == pin:
    print("\n Welcome to python ATM!")
    while True:

        print("\n======= ATM MENU =======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Help")
        print("5. Exit")

        choice = int(input ("Enter your choice: "))

        if choice ==1:
            print("Current Balance = Rs.", balance)
        
        elif choice ==2:
           amount =  int(input("Enter amount to deposit: Rs. "))
           if amount <=0:
               print("Invalid amount")
               continue
           balance = balance + amount 
           print("Money deposited sucessfully!")
           print("Updated balance: ", balance)

        elif choice == 3:
            amount = int(input ("Enter amunt to withdraw: Rs. "))

            if amount > balance:
                print("Insufficient Balance!")
            
            else: 
                balance = balance - amount 
                print("Please collect you cash")
                print("Remaining balance =", balance)

        elif choice == 4: 
            pass
            
            print("\nHelp")
            print("1 - Check Balance")
            print("2 - Deposit Money")
            print("3 - Withdraw Money")
            print("4 - Exit ATM")

        elif choice == 5:
            print("Thank you for visiting!")
            break
        else: 
            print("Invalid choice!")
else:
    print("Incorrect pin")

