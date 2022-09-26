import math
def s(x,y,z):
    p=(x+y+z)/2
    s=math.sqrt(p*(p-x)*(p-y)*(p-z))
    return s
A=[]
for i in range (3):
    print ('Введите стороны', i ,'-го треугольника:')
    a=int (input('a:'))
    b=int (input('b:'))
    c=int (input('c:'))
    A.append(s(a,b,c))
    for i in range (3):
        print ('Площадь',i,'-го треугольника {:.2f})'.format(A[i]))
    if A[0]==A[1]:
        if A[0]==A[2]:
            print('Треугольники равновеликие')
else: print('Треугольники не равновеликие')

