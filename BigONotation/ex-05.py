def ex05(nested_list):
    total = 0 # O(1)
    for inner_list in nested_list: # O(n)
        for num in inner_list: # O(m)
            total += num 
            
        for num in inner_list: # O(m)
            total += num
            
        for num in inner_list: # (m)
            total += num
    return total # O(1)

# Equation : 1 + n(3m) + 1 -> mn
# O(mn)       