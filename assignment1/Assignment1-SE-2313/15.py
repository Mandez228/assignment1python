print("Enter numbers separated by space:")
a, b, c, d = map(int, input().split())
x = a + b + c + d
y1 = a - b - c - d
y2 = abs(a - b - c - d)
z = a * b * c * d
print(f"Sum: ({a})+({b})+({c})+({d})={x}")
print(f"Difference#1: ({a})-({b})-({c})-({d})={y1}")
print(f"Difference#2: |{y1}|={y2}")
print(f"Product of {a}*{b}*{c}*{d}={z}")
