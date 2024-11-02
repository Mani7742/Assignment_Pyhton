# 14. Write a program that breaks the loop when a certain condition is met.
for i in range(1, 21):
    if i == 15:
        print("Loop is broken at 15.")
        break
    print(i)