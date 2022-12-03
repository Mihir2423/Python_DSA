#Program to return all the subset (Power set)

def recur_(i,res,arr,subset):
    if i == len(arr):
        res.append(subset.copy())
        return
    subset.append(arr[i])
    recur_(i+1, res,arr,subset)
    subset.pop()
    recur_(i+1, res,arr,subset)
    
    

def power_(arr):
    res = []
    subset = []
    recur_(0,res,arr,subset)
    return res

nums = [1,2,3]
print(power_(nums))