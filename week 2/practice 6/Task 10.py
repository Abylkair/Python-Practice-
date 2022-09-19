lst = [1,2,3,4,5,5,6,6,7]
print(*filter(lambda x : lst.count(x) > 1, lst))
