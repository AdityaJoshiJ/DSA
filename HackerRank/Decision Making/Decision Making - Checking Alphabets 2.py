n = input()

if n.isalpha():
    n = n.lower()

    if n in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
