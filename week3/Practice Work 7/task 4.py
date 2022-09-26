def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a, b, c, d = map(int, input().split())
x = a * d
y = b * c
z = gcd(x, y)
print(x // z, '/', y // z, sep='')
