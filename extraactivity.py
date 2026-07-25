name = input ("Enter customer name: ")
customer_id = name[:3].upper()+name [-1].upper()
prices = [120, 250, 80, 60, 150]
print("\nOriginal price list: ", prices)

total = 0 
for price in prices:
    total +=price

average = total/len(prices)
prices.sort()

smallest = prices[0]
largest = prices[-1]
reverse_prices = prices[::-1]

bill_text = str(total)

print("\n========== SHOPPING SUMMARY ==========")
print("customer id: ", customer_id)
print("total bill: ", bill_text)
print("average item price: ", average)
print("cheapest item: ", smallest)
print("Costliest item: ", largest )
print("reverse sorted prices: ", reverse_prices)