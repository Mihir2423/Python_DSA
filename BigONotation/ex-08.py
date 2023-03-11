def ex08(n):
    if n == 0:
        return 
    
    print(n)
    ex08(round(n/2))
    
# O(log2(n))