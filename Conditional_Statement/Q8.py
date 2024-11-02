# 8. Create a program that checks if a given string is a palindrome.
string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")