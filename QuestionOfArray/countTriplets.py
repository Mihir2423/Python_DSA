def countTriplet(arr, n):		# code here
    c = 0
    arr.sort()
    for i in range(n-1,1,-1):
        j = 0
        k = i-1
        while j < k:
            if arr[j] + arr[k] == arr[i]:
                c+=1
                j+=1
                k-=1
            elif arr[j] + arr[k] < arr[i]:
                j=j+1
            else:
                k=k-1
    return c

print(countTriplet([1,5,3,2], 4))
            