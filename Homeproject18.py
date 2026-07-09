try: 
    age = int(input("Please enter your age: "))

except ValueError:
    print("Please enter integers only")

if age%2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")


