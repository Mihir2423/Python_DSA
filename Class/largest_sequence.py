arr = list(map(int, input("Enter a sequence of numebers: ").split()))

max_ = arr[0]
for i in arr:
    if max_ < i:
        max_ = i

print(f"Largest in given sequence is {max_}")