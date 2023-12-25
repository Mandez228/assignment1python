import math
print("Parameters of right-angled triangle")
a = float(input("Enter 1st leg: "))
b = float(input("Enter 2nd leg: "))
c = math.sqrt(a**2 + b**2)
print("Hypotenuse of triangle is:", c)
P = a + b + c
print("Perimeter of triangle is:", P)
