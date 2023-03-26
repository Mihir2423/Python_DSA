def insertion_sort(myList):
    for i in range(len(myList)-1):
        min_index = i
        for j in range(i+1, len(myList)):
            if myList[j] < myList[min_index]:
                min_index = j
        myList[min_index], myList[i] = myList[i], myList[min_index]
    return myList



print(insertion_sort([3,2,1,5,6,7]))