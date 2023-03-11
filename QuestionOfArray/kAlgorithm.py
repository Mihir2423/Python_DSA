def maxSubArraySum(arr,N):
    ##Your code here
    max_sum = -1000000
    curr_sum = 0
    flag = False
    for i in range(N):
        if arr[i] > 0:
            flag = True
    if not flag:
        return max(arr)
    end = 0
    while end < N:
        curr_sum += arr[end]
        end += 1
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
            
    return max_sum

print(maxSubArraySum([1, 2, 3, -99, 8,1], 6))