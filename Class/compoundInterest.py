p = float(input("Enter prinicipal : "))
r = float(input("Enter rate : "))
t = float(input("Enter time : "))
n = float(input("Enter number of times interest applied per time period : "))

ci = p * ((1 + (r/n))**(n*t))

print("Compound Interest : ", ci-p)