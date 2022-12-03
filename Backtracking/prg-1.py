# Find all the permutations of a given string

def findPermutation(a, left, right):
    if left == right:
        print(toString(a))
    else:
        for i in range(left, right):
            a[left], a[i] = a[i], a[left]
            findPermutation(a,left+1,right)
            a[left], a[i] = a[i], a[left] #backtracking

def toString(a):
    return ''.join(a)



string = "ABCD"
a = list(string)
n = len(string) 
findPermutation(a, 0, n)


            