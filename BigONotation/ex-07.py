def ex07(lst, search_lst):
    max_val = max(lst) # O(n)
    
    for value in search_lst: # O(m)
        if max_val == value:
            return True
        
    return False

# O(n + m)