
k = int(input())
for i in range(1, k + 1):
   n = len(str(i))
   summ = 0
   for j in str(i):
       summ += int(j) ** n
   if i == summ:
       print(i, end=' ')


def tang(a1, a2):
   tan = a2 / a1
   return tan
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
z1 = int(input())
z2 = int(input())
if tang(x1, x2) < tang(y1, y2) < tang(z1, z2):
   print(f'X({x1, x2})')
elif tang(y1, y2) < tang(x1, x2) < tang(z1, z2):
   print(f'Y({y1, y2})')
else:
   print(f'Z({z1, z2}')