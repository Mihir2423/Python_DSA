def merge(arr1,arr2,n,m):
    #code here
    i = n-1
    j = 0
    while i >= 0 and j < m:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1
        
    arr1.sort()
    arr2.sort()
    
arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]

merge(arr1,arr2,4,5)

print(*arr1, end=" ")
print(*arr2)