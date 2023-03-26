def merge_list(list1, list2):
    res = []
    max_ele = 1000000
    list1.append(max_ele)
    list2.append(max_ele)
    i,j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i+=1
        else:
            res.append(list2[j])
            j+=1
    res.pop()
    return res

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list) / 2)
    left = my_list[:mid]
    right = my_list[mid:]   
    return merge_list(merge_sort(left), merge_sort(right))

print(merge_sort([3,1,4,2]))    
