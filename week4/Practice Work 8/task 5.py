from random import randint
N, M = 4, 3
lst = [[randint(-50, 50) for _ in range(M)] for _ in range(N)]
print(list([(1 if min(i) % 2 else 0) if j == min(i) else j for j in i] for i in lst))