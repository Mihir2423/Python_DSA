def subArraySum(arr, n, s):
    if s == 0:
        return [-1]
    t = arr[0]
    start = 0
    end = 0
    while end < n:
        if t == s:
            return [start+1, end+1]
        elif t < s :
            end+=1
            if end < n:
                t += arr[end]
        else:
            t-=arr[start]
            start+=1
    return [-1]


arr = [1,2,3,4,5,6,7,8,9,10]
n = 10
s = 15
print(subArraySum(arr, n, s))