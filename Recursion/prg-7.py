def recur(ind, sum, arr, n, sumSubset):
        if ind == n:
            sumSubset.append(sum)
            return
        recur(ind+1, sum+ arr[ind], arr, n, sumSubset)
        recur(ind+1, sum, arr, n, sumSubset)
    
    
def subsetSums( arr, N):
	sumSubset = []
	recur(0,0,arr,N,sumSubset)
	sumSubset.sort()
	return sumSubset

    

arr = [5,2,1]    
print(subsetSums(arr,3))


#Program to calculate all the subset sum using recursion