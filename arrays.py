def isSorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


def removeduplicate(arr):
    i = 0 
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return arr

def rotateArray(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(n - 1):
        arr[i] = arr[i+1]
    arr[n - 1] = temp
    return arr

arr = [1, 2, 3, 4, 5]
print(rotateArray(arr))