# 13. Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/' and num2 != 0:
    print("Result:", num1 / num2)
else:
    print("Invalid operator or division by zero.")