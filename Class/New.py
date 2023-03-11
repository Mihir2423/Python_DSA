t = int(input())
for i in range(t): 
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr = sorted(arr)
    su,count = 0,0
    for i in range(len(arr)):
        su += arr[i] 
        if su <= n:
            count +=1
        elif su>n:
            break
    print(count)