a = 1 
b = 3 
c = 1
d = 5

l = a * d + b * c
k = b * d

A, B = l, k
while A != B:
    if a > b:
        A -= B
    else:
        B -= A
print (f'{l // A}/{k // a}')