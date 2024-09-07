def min(arr, start):
    min = sum(arr)
    for i in range(start, len(arr)):
        if arr[i] < min:
            min = arr[i]
    return arr.index(min)


def selec(arr):
    j = 0
    for i in range(len(arr)):
        t = min(arr, j)
        arr[i], arr[t] = arr[t], arr[i]
        j += 1
    print(arr)


arr = list(map(int,input().split()))
selec(arr)