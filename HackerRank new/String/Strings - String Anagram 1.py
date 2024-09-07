str = input()
str2 = input()
tmp = list(str)
tmp2 = list(str2)
allEqual = False
for i in range(0, len(str)):
    if tmp[i] in tmp2:
        allEqual = True
    else:
        allEqual = False
if allEqual == True:
    print("Anagram")
else:
    print("Not Anagram")
