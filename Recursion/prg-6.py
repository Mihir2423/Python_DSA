# First uupercase letter in a string

from curses.ascii import isupper


def uppercase_str(word):
    if word == '':
        return False
    if word[0].isupper():
        return word[0]
    return uppercase_str(word[1:])


word = input("Enter a word: ")

if uppercase_str(word):
    print(uppercase_str(word))
else:
    print("No uppercase letter")