def recur(i,arr,n,subset ,res):
    if i == n:
        res.append(subset.copy())
        return 
    subset.append(arr[i]) 
    recur(i+1, arr, n, subset ,res) 
    subset.pop()
    while i + 1 < len(arr) and arr[i] == arr[i+1]: 
        i += 1
    recur(i+1, arr, n, subset,res)
    
arr = [1,2,2]
arr.sort()
res  = []
recur(0,arr,3,[], res)
print(res)


# [5,2,1] = [5], [5,2], [5,2,1], [5,1], [2], [2,1], [1], []

# Tree recursion --> 1 st - > base class(condition) -> 2 nd -> left subtree logic -> 3rd step -> Backtracking -> 4th-> right subtree logic