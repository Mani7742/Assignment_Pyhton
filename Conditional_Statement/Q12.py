# 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
temp = float(input("Enter temperature in Celsius: "))
if temp <= 0:
    print("It's freezing.")
elif temp < 30:
    print("It's moderate.")
else:
    print("It's hot.")