# Palindrome Partitioning

def recur(i,s,part,sub,n):
    if i >= n:
        part.append(sub.copy())
        return
    for j in range(i,len(s)):
        if isPalin(s,i,j) == True:
            sub.append(s[i:j+1])
            recur(j+1,s,part,sub,n)
            sub.pop()


def isPalin(s,i,j):
    while i<j:
        if s[i] != s[j]:
            return False
        i,j = i+1, j-1
    return True 

part = []

recur(0,"aab", part, [],len("aab"))

print(part)