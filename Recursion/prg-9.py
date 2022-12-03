#program to print all the unique subset

def subsetsWithDup(nums):
        res = []
        nums.sort()
        def recur_(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            recur_(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            recur_(i+1, subset)
        recur_(0, [])
        return res


arr = [1,2,2]
print(subsetsWithDup(arr))