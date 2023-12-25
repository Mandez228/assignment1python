import math
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if (a < 0) or (b < 0):
    print("Invalid input")
else:
    am = (a + b) / 2
    gm = math.sqrt(a * b)
    print("Arithmetic mean: ", am)
    print("Geometric mean: ", gm)