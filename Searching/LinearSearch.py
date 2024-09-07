arr = list(map(int, input().split()))
k = int(input())
flag = False
for i in range(len(arr)):
    if arr[i] == k:
        print(f"Found {k} at {i}th index")
        flag = True
        break
if flag == False:
    print(f"{k} is not found")
