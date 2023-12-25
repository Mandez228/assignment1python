x = int(input("Enter a 4digit number: "))
is4 = str(x)
if len(is4) == 4 and (x > 0):
    a = x // 1000
    b = x % 1000 // 100
    c = x % 100 // 10
    d = x % 10
    print(f"{a}+{b}+{c}+{d}={a+b+c+d}")
else:
    print("Invalid input entered")