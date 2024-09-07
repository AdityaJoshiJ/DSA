arr = list(map(int, input().split()))
x = arr[0]
a = arr[1]
# print(x, a)
# i = a
new = []

def divisor(n):
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)
    return div

flag=True
for n in range(0, x):
    z = divisor(n)
    for i in range(0, len(z)):
        if x == n*a+z[i]:
            new.append(n)
            flag=False
if(flag==True):
    print("None")
else:
    print(new[0])