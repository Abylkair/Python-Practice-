def func(a):
    a[0], a[-1] = a[-1], a[0]
    return a
 
n = int(input('m = '))
a = list(map(int, input('in one line separated by a space ').split(maxsplit = n)))
 
print(a)
print(func(a))