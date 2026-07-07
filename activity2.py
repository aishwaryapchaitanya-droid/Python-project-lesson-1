try:
    num1, num2 = eval(input("Enter ttwo numbers seperated by a comma: "))
    result = num1 / num2 
    print("Result is ", result)

except ZeroDivisionError:
    print("Division by zero is error!")

except SyntaxError:
    print("Comma is missing. Enter number seperated by comma like this 1,2")

except:
    print("Wrong input")

else:
    print("Exceptions")

finally:
    print("This will execute no matter what")
    