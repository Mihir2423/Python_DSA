# Chained Operation
# ? Prg to use "and" and "or"

x, y = map(int, input("Enter two number with space : ").split())

if x == y and x % 2 == 0:
    print("X wins")
elif x != y or y % 2 == 0:
    print("Y wins")
else:
    print("No Winner")

#! Ternary Operation

# ? Prg to use ternary operator

# * Syntax
"""
[on_true] if [expression] else [on_false]
"""

a = input("Enter a word: ")
b = input("Enter another word: ")
print("Yes" if len(a) == len(b) else "No")
