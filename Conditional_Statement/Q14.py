# 14. Check if a year input by the user is a century year.
year = int(input("Enter a year: "))
if year % 100 == 0:
    print("It's a century year.")
else:
    print("It's not a century year.")