# 20. Create a program that simulates a countdown timer starting from a given number down to zero.
countdown = int(input("Enter the starting number for countdown: "))
for i in range(countdown, -1, -1):
    print(i)