def ex03(nums):
    result = [1 for _ in range(len(nums))] # O(n)
    
    for i, num1 in enumerate(nums): # O(n)
        for num2 in nums: # O(n)
            if num1 == num2:
                continue
            result[i] *= num2
    # Inner loop will run n times -> Therefore, equation will be -> n + n(3n) + 1 -> n^2
    return result

# O(n^2)