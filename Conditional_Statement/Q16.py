# 16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a == b == c:
    print("It's an equilateral triangle.")
elif a == b or b == c or a == c:
    print("It's an isosceles triangle.")
else:
    print("It's a scalene triangle.")