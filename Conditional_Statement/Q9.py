# 9. Take three sides of a triangle as input and check if they form a valid triangle.
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a + b > c and b + c > a and c + a > b:
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")