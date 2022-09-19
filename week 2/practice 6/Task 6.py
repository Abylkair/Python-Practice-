import random
arr = [random.randint(0,100) for _ in range(10)]
print(len(list(filter(lambda x: x < max(arr), arr))), len(list(filter(lambda x: x > min(arr), arr))))
 
print(sum(filter(lambda x: x > 5, [int(input()) for _ in range(10)])))