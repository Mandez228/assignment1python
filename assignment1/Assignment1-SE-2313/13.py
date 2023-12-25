K = int(input("Enter K: "))
x = K % 7
weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
weekday = weekdays[x]
if 1 <= K <= 365:
    print(f"{K} day of the year is: {weekday}")
else:
    print("Invalid enter")
