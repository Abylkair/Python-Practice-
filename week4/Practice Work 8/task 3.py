N = 3

A = [[1, 2, 3]
     [2, 5, 6]
     [3, 6, 4]]

b = "yes"

for i in range(N):
    for j in range(N):
        if A[i][j] != A[j][i]:
            b = "no"

print(b)