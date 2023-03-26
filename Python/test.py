import pyautogui
import time

time.sleep(3)
pyautogui.write("""s1a=input("data1: ")
s1b=input("data2: ")
s2a=input("data3: ")
s2b=input("data4: ")
l1a=s1a.split(",")
for i in range(len(l1a)):
	l1a[i]=int(l1a[i])
l1b=s1b.split(",")
for i in range(len(l1b)):
	l1b[i]=int(l1b[i])
d1=dict(zip(l1a,l1b))
l2a=s2a.split(",")
for i in range(len(l2a)):
	l2a[i]=int(l2a[i])
l2b=s2b.split(",")
for i in range(len(l2b)):
	l2b[i]=int(l2b[i])
d2=dict(zip(l2a,l2b))
l3a=[]
l3b=[]
for i in d1.keys():
	if i in d2.keys():
		l3a.append(i)
		l3b.append(2*d1[i])
d3=dict(zip(l3a,l3b))
d3=sorted(d3.items())
print("common keys:",d3)""", interval=0)