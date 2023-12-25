import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
if (a < 0) or (b < 0):
    print("Invalid input")
else:
    print("The Geometric Mean is:", math.sqrt(a * b))
