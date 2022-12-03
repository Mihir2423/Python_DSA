a = [1,3,5,7,9]
b = [0,2,4,19,20]

c = []
for i in range(len(a)+len(b)):
    if i < len(a):
        c.append(a[i])
    else:
        c.append(b[i-len(a)])
        
print(c)