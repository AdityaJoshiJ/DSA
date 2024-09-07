total = int(input())
benP = int(input())
blackP = int(input())
ben = (total*benP)//100
black = ((total-ben)*blackP)//100
other = (total-ben-black)//3
print(ben)
print(black)
print(other)
