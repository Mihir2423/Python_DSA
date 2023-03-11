# List

#? Defintion : Lists are used to store multiple items in a single variable.

List = ["apple", "banana", "litchi", "cherry"]

#! Append
List.append("Mihir")

#! Insert
arr = [1, 2, 3, 4]
List.extend(arr[:])

# ? Syntax
"""
List.insert(postion, val)
"""
List.insert(0, "Insertion")
#! Remove
List.remove("Insertion")  # pops out Insertion

#! Pop
# * Removes or pops out element of given index or last index if nothing is providied
List.pop()  # pops out 4
List.pop(1)  # pops out banana

#! Clear
arr.clear()
print("Array -> ", arr)

#! Index
print("Index of 1 : ", List.index(1))

#! Count
arr_ = [1, 1, 1, 1, 1]
print("No. of 1 in arr : ", arr_.count(1))

#! Sorting
_arr_ = [3, 5, 26, 1]
_arr_.sort()
print("Sorted Array : ", _arr_)

#! Reversed
_arr_.reverse()
print("Reversed Array : ", _arr_)
print("List : ", List)

#! Copy
arr_c = _arr_.copy()
print("Copied Array : ", arr_c)

#! Tuples

t = (1,2,3,"hello")
print(t)
