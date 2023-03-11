# Strings

a = "Hello"
print("Given String : ",a)
print("Length of a string :",len(a))

#! Slicing

b = "Hello World!"
'''
    b[:] -> Whole String
    b[:5] -> Starting to index 5 
    b[5:] -> Index 5 to End
    b[a:b] -> Index a to Index b-1
'''
print("Sliced String : ",b[6:len(b)])

#! Modify String

a = "Hello World!"
print(a.upper())

print(a.lower())

b = "  Hello World!  "
print(b.strip())

print(a.replace('!','.'))
print(a.replace('l','b'))

print(a.split(' '))

#! Concatinate String

first_name = "Mihir"
Last_name = "Aman"

print(first_name+Last_name)

#! Format String

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#! Other functions

a = "hello, World!"

print(a.capitalize())

print(a.casefold())

print(a.endswith('!'))

print(a.count('l'))

print(a.index('l'))

b = a.split(' ')
print("/".join(b))


print(a.find("World"))
#? Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)
