# 15. Write a program to check if a number is within a specified range.
num = int(input("Enter a number: "))
low, high = 10, 100
if low <= num <= high:
    print("The number is within the range.")
else:
    print("The number is outside the range.")