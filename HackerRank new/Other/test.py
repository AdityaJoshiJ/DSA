import math
n=3
m=1
p=2
e=1
def combination(n,r):
    com=math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
    return com
total=combination(n,p)*combination(m,e)
print(total)