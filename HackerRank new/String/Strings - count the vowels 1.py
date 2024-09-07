str = input()
str = str.lower()
v = ['a', 'e', 'o', 'u', 'i']
count = 0
for i in range(0, len(str)):
    if str[i] in v:
        count += 1
print(f"Number of vowels: {count}")
