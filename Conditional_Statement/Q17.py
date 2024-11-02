# 17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.
num = int(input("Enter an integer: "))
if num % 2 == 0 and num % 3 == 0:
    print("The number is divisible by both 2 and 3.")
elif num % 2 == 0:
    print("The number is divisible by 2.")
elif num % 3 == 0:
    print("The number is divisible by 3.")
else:
    print("The number is not divisible by 2 or 3.")