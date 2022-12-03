# Length of a string using recursion

def str_len(word):
    if word == '':
        return 0
    return 1 + str_len(word[1:])

print(str_len('Mihir'))


# 1 + str_len('ihir') => 1 + 1 + 1 + 1 + 1 + 0 = 5 <Ans>
# 1 + str_len('hir') => 1 + 1 + 1 + 1 + 0
# 1 + str_len('ir') => 1 + 1 + 1 + 0 
# 1 + str_len('r') => 1 + 1 + 0 
# 1 + str_len('') => 1 + 0