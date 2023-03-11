def ex09(strings):
    for i, string in enumerate(strings): # O(n)
        digits = 0
        
        for char in string: # O(m)
            if char in [str[i] for i in range(0, 10)]:
                digits += 1
            
        if digits >= len(string) / 2:
            strings[i] = sorted(strings[i]) # O(mlog2(m))
    return strings

# Equation : n(m + mlog(m)) -> nmlog2(m)
# O(nmlog2(m))