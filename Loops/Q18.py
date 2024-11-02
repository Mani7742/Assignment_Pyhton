# 18. Use a loop to print numbers in reverse order within a given range.
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for i in range(start, end - 1, -1):
    print(i)