def binarySearch(arr, k):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            print(mid)
            break
        elif k < arr[mid]:
            high = mid-1
        else:
            low = mid+1


arr = list(map(int, input().split()))
k = int(input())
binarySearch(arr, k)
