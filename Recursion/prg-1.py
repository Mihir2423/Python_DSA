#Square of a number

def square_tail_rec(n): # Recursive function, Time Complexity --> O(n)
    if n > 0: # Base Class 
        k = n**2
        print(k)
        square_tail_rec(n-1) #Tail-Recursion 
        
def square_head_rec(n): # Recursive function, Time Complexity --> O(n)
    if n > 0: # Base Class 
        square_head_rec(n-1) #Head-Recursion 
        k = n**2
        print(k)


def square_iter(n): #Time Complexity -> O(n)
    while n > 0: # Iterative function 
        k = n**2
        print(k)
        n -= 1

print("Tail Recursion \n")
square_tail_rec(4)
print("\n Head Recursion \n")
square_head_rec(4)
print("\n Iterative Function \n")
square_iter(4)