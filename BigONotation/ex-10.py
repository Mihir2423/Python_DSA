def ex10(dict1, dict2):
    keys1 = sorted(dict1.keys()) # O(nlog2(n))
    keys2 = sorted(dict2.keys()) # O(mlog2(m))
    
    process = keys1 + keys2 
    result = set()
    
    while len(process) > 0: # O((m + n)k)
        element = process.pop(0)
        result.append(element)
        
        if len(element) == 1:
            continue
        process.append(element[:-1])
    
    return result

# O(nlog2(n) + mlog2(m) + (m + n)k)