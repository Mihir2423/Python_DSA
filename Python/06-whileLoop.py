# While loop

#! Syntax
'''
while condition == True:
    do this
    break
'''

#? Prg to implement While loop

t = 1

while t < 5:
    print(f"Yes {t} time")
    t += 1
    
while True:
    a = int(input("\nEnter numbers to print them and '0' to exit: "))
    if a == 0:
        print("\nExited...")
        break
    else:
        print(f"Your Number : {a}")