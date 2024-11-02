# 15. Print the sum of even and odd numbers separately up to a given number.
limit = int(input("Enter the limit: "))
even_sum = sum(i for i in range(2, limit + 1, 2))
odd_sum = sum(i for i in range(1, limit + 1, 2))
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)