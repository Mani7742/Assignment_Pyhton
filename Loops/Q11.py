# 11. Print the reverse of a given number.
num = int(input("Enter a number to reverse: "))
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10
print("Reversed number:", reverse)