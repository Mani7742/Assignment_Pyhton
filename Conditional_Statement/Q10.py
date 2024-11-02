# 10. Write a program to determine if a given character is a vowel or consonant.
char = input("Enter a character: ").lower()
if char in "aeiou":
    print("The character is a vowel.")
else:
    print("The character is a consonant.")