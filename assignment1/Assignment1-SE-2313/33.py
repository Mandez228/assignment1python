import math
x1, y1 = map(int, input("Enter first coordinates(x1 y1): ").split())
x2, y2 = map(int, input("Enter second coordinates(x2 y2): ").split())
x3, y3 = map(int, input("Enter third coordinates(x3 y3): ").split())

dist1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
dist2 = math.sqrt((x3-x2)**2 + (y3-y1)**2)
dist3 = math.sqrt((x3-x1)**2 + (y3-y1)**2)
P = dist1 + dist2 + dist3
print("Perimeter of the triangle is", P)
