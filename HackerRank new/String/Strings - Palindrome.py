str = input()
str = str.lower()
rev = str[::-1]
if (str == rev):
    print("Palindrome")
else:
    print("Not a Palindrome")
