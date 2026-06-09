#Taking total amount as input from user
Amount = int(input("Please enter amount for withdraw: "))

#Calculating the number of notes from different denominations
note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount %100)%50)//10

print("notes of 100 rupee", note1)
print("notes of 50 rupee", note2)
print("notes of 10 rupee", note3)

