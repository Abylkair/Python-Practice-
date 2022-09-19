a=[]
for i in range(10):
    a.append(i)
x=a[0]
for i in a:
    if i > x and i % 2 == 0:
        x=i
print(x)

a=[]
for i in range(20):
    a.append(i)
b=[]
for i in a:
    if i % 2 == 0 and i < 10:
        b.append(i)
if len(b) == 0:
    print("There are no numbers according to the given condition.")
else:
    print(b)