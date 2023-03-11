arr1 = [1, 3, 5, 7]
n = len(arr1)

arr2 = [0, 2, 6, 8, 9]
m = len(arr2)
c = []
for i in range(n):
    c.append(arr1[i])
for i in range(m):
    c.append(arr2[i])
c.sort()

print(c[:n], c[n:n+m])