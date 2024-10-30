months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
    }

Month = int(input("Enter a number that corresponds to a month (1-12): "))
if Month <13:
    print(months[Month])
else:
    print("This number does not correspond to a month")