def ex04(nums1, nums2):
    results = [] # O(1)
    
    for num in nums1: # O(n)
        results.append(num) # O(1)
    
    for i, num in enumerate(nums2): # O(m)
        if i >= len(results): # O(1)
            results.append(1) # O(1)
        results[i] *= num # O(1)
    return results # O(1)

# Equation : 1 + n + 3m + 1 -> n + m
# O(n + m)