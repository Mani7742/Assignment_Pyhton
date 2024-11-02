# 10. Use a loop to count the number of digits in an integer.
num = int(input("Enter an integer: "))
digit_count = 0
while num > 0:
    num //= 10
    digit_count += 1
print("Number of digits:", digit_count)