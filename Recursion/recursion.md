Recursive Function --> 
1. A function that makes call to itself 
2. It has a base class at which the recursive function returns

Recurrence Relation -->
T(n) = [T(n-1) + n ; n>1 \\ 1 ; n = 1]
--> T(n) = T(n-1) + n
--> T(n-1) = T(n-2) + n-1
--> T(n-2) = T(n-3) + n-3

Substitution:
T(n) = T(n-1) + n
T(n) = T(n-2) + n-1 + n
T(n) = T(n-3) + n-2 + n-1 + n
.
.
.
T(n) = T(n-k) + n-k-1 + .... (n-2) + (n-1) + n
when n-k = 1 => k = n-1

So, T(n) = T(n-(n-1) + (n-(n-1)-1) + .... (n-2) + (n-1) + n
         = T(n-n+1) + (n-n+1-1) + .... (n-2) + (n-1) + n
         = T(1) + .... + (n-2) + (n-1) + n
         = 1 + .... + (n-2) + (n-1) + n
         = n(n+1)/2
         = (n^2 + n)/2

    T(n) = O((n^2 + n)/2) = O(n^2)

Types of Recursion:
1. Head Recursion = First statement in recursion after base condition
2. Tail Recursion = No statement after the recursive call
3. Tree Recursion = When a function call itself more than once, it forms the pattern of tree (Time Complexity = 2^n where n is input)
4. Indirect Recursion



# Recursion problem solving
Let f(n) be a recursive function:
1. Show f(1) works (base class)
2. Assume f(n-1) works
3. Show f(n) works using f(n-1)