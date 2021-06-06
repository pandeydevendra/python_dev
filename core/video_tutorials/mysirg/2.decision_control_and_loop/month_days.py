month_days = {
    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31
}
num_month = input("Enter the value for month: ")
if 0 < int(num_month) < 13:
    num_days = month_days[num_month]
    print(f"Month {num_month} has {num_days} days.")
else:
    print("Month value is not correct!!!")
