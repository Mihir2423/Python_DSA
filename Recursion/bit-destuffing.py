arr = list(map(int, input("Enter bits in comma separated form eg(1,1,1): ").split(",")))
print(arr)
c = 0
for i in range(len(arr)):
    if arr[i] == 1:
        c += 1
        print(arr[i], end=" ")
    else:
        count = 0
        print(arr[i], end=" ")
    if c == 5:
        print(1, end=" ")
        c = 0
        i += 1