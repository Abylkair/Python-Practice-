list = sorted(input(' a b c > ').split())
print(sum((list == sorted(list(str(n))) for n in range(100,int(input())))))
