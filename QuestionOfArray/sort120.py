def sort012(arr, n):
    mid,low,high = 0,0,n-1
    while mid <= high:
        if arr[mid] == 0:
            arr[mid],arr[low] = arr[low],arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1
        
arr = [0, 1, 2, 0, 1, 2]

sort012(arr, 6) 


print(*arr)