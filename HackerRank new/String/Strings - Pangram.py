n = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
n = n.lower()
flage =True
for i in alphabet:
    if i not in n:
        flage=False
if flage == True:
    print("Pangram")
else:
    print("Not a Pangram")
