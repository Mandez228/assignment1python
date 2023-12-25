import math
x1, y1 = map(int, input("Enter coordinates (x1 y1): ").split())
x2, y2 = map(int, input("Enter coordinates (x2 y2): ").split())
dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"The distance between two points is {dist}")