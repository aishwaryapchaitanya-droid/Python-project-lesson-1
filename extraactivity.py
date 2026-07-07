print("🍕 Welcome to pizza shope!")
try:
    quantity = int(input("Enter the number of pizzas: "))
    price = int(input("Enter the price of one pizza: "))
    total = quantity*price

except ValueError:
    print("PLease enter numbers only.")

else:
    print("Total bill = ", total)
    print("Thank you for your order! ")

finally:
    print("Visit Again!")
