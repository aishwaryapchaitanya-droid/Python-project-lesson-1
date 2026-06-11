actual_cost = float(input("Please Enter the actual product price: "))
sale_amount = float(input("Please Enter the Sale amount: "))

if (sale_amount > actual_cost ):
    amount = sale_amount - actual_cost
    print("total profit = {0}", (amount))

else:
    print('No profit!!')
