def add(p,q):
    return(p+q)
def subtract(p,q):
    return(p-q)
def multiply(p,q):
    return(p*q)
def divide(p,q):
    return(p/q)

try: 
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))


except ZeroDivisionError:
    print("not divisible by 0. num2 should be greater than 0.")
except ValueError:
    print("Enter numbers only")


print("1. Addition")
print("2. Subtraction")
print("3.Multiplication")
print("4. Division")
user_choice = (input("Pick one of the above operations: "))


if user_choice == '1': 
    sum = num1+num2
    print("Result = ", sum)
    

elif user_choice == '2':
    Sub = num1 - num2 
    print("Result = ", Sub)

elif user_choice == '3':
    Mul = num1*num2
    print("Result = ", Mul)

elif user_choice == '4':
    Div = num1/num2
    print("Result = ", Div)

else:
    print("Invalid choice")




