# Sum of n natural numbers using recursion 

def sum_rec(n):
    if n == 1:
        return 1
    return sum_rec(n-1) + n #Time_complexity = O(n)


num = int(input("Enter a number: "))

print(f"\n Sum of {num} natural number : {sum_rec(num)}")