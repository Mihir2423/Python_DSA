def rearrange(arr, n):
    max_, min_ = n - 1, 0
    m = arr[max_] + 1
    for i in range(n):
        if i % 2 == 0:
            arr[i] += ((arr[max_] % m) * m)
            max_ -= 1
        else:
            arr[i] += ((arr[min_] % m) * m)
            min_ += 1
    for i in range(n):
        arr[i] = arr[i] // m


arr = [1, 2, 3, 4, 5, 6]
rearrange(arr, 6)

print(*arr)