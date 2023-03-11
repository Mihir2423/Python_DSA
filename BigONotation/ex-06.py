def ex06(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    last = ex06(n - 1)
    second_last = ex06(n - 2)
    return last + second_last

fib = ex06(4)
print(fib)

# O(2^n)

