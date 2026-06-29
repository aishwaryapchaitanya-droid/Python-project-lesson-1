num = input("Enter a number: ")
length = len(num)
start = (length  - 1)//2
end = length//2
product = 1
for i in range (start, end + 1):
    for j in num [i]:
        product = product * int (j)

print("product of middle digit(s) = ", product)