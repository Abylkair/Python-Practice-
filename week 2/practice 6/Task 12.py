n=int (input())
a=[]
for _ in range(n):
    a.append(float(input()))
print (a)
m = a[0]
for i in a:
    if abs (i) <m:
        m = i
print (m)
print (a[::-1])
import random
a=[]
b=[]
for _ in range (10):
    a.append(randint(-10,10))
    b.append(randint(-10,10))
print (a)
print (b)
a,b = b,a 
print (a)
print (b)