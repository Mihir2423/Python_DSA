def pivot(myList, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if myList[pivot_index] > myList[i]:
            swap_index += 1
            myList[swap_index], myList[i] = myList[i], myList[swap_index]
    myList[pivot_index], myList[swap_index] = myList[swap_index], myList[pivot_index]
    return swap_index


def quick_sort_helper(myList, left, right):
    if left < right:
        pivot_index = pivot(myList, left, right)
        quick_sort_helper(myList, left, pivot_index - 1)
        quick_sort_helper(myList, pivot_index + 1, right)
    return myList

def quick_sort(myList):
    return quick_sort_helper(myList, 0, len(myList)-1)


myList = [4,6,1,7,3,2,5]
quick_sort(myList)
print(myList)

# best case , average case = O(nlogn)
# worst case = O(n^2)