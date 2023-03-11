def find_subarrays_with_repeats(a, b):
    subarrays = []
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            subarray = a[i:j]
            counts = {}
            for element in subarray:
                if element in counts:
                    counts[element] += 1
                else:
                    counts[element] = 1
            if sum(count >= 2 for count in counts.values()) == b:
                subarrays.append(subarray)
    
    return len(subarrays)



arr = [1,2,3,1,2,3]
b = 2
print(find_subarrays_with_repeats(arr,b))