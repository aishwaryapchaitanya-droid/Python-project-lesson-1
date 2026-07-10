import math
angle = float(input("Enter the angle in degress: "))

radians = math.radians(angle)
sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)
print("\nTrigonometric Values")
print("sin(", angle, ") =", sin_value)
print("cos(", angle, ") =", cos_value)
print("tan(", angle, ") =", tan_value)