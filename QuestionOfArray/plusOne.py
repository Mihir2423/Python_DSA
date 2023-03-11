def plusOne(digits):
    n = int("".join(map(str, digits)))
    n = n + 1
    res = list(str(n))
    res = list(map(int, res))
    return res


print(plusOne([9]))
