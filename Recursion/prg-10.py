# Combinational Sub 1


def comb_sum(ind, target, arr, subArr, res):
    if ind == len(arr):
        if target == 0:
            res.append(subArr.copy())
        return
    if target - arr[ind] >= 0:
        subArr.append(arr[ind])
        comb_sum(ind, target - arr[ind], arr, subArr, res)
        subArr.pop()
    comb_sum(ind+1, target, arr, subArr, res)
        

res = []
(comb_sum(0,7,[2,3,5,7], [], res))
print(res)
