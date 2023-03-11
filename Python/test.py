#Sub Array sum

arr = [1,2,3,4]
target = 5
s = 0
start = 0
flag = False

for i in range(len(arr)):
    s += arr[i]
    while s > target:
        s -= arr[start]
        start += 1
    if s == target:
        flag = True
        print(arr[start : i+1])
        break
if flag == False:
    print("Cannot find the subArray")
