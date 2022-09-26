from random import randint as rd
def arrmax(arr) :
    bmax = arr[0][0]
    n = len(arr)
    for i in range(n) :
        if max(arr[i]) > bmax :
            bmax = max(arr[i])
    return bmax
def arrprint(a, b) :
    for i in a :
        print(*i)
    print()
    for i in b :
        print(*i)
    print()
 
print('enter the number of rows for the first array : ')
na = int(input())
print('number of items in a row : ')
ma = int(input())
print('enter the number of rows for the first array : ')
nb = int(input())
print('number of items in a row : ')
mb = int(input())
 
a = [[rd(1,50) for i in range(ma)] for j in range(na)]
b = [[rd(51,100) for i in range(mb)] for j in range(nb)]
 
arrprint(a,b)
 
amax = arrmax(a)
bmax = arrmax(b)