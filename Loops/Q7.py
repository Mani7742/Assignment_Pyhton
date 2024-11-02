# 7. Find the factorial of a number using a while loop.
num = int(input("Enter a number to find its factorial: "))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print("Factorial:", factorial)