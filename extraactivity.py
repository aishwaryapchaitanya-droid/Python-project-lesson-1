#Function to calculate the perimeter of the square
def square_perimeter (side):
    perimeter = 4*side
    print("perimeter of square", perimeter)

side = float(input("Enter the side of the square: "))

square_perimeter(side)