def smallestInRow(mat, n, m):
    print("{", end = "")
    for i in range(n):
        minm = mat[i][0]
        for j in range(1, m, 1):
            if (mat[i][j] < minm):
                minm = mat[i][j]
        print(minm, end = ",")
 
    print("}")
def smallestInCol(mat, n, m):
    print("{", end = "")
    for i in range(m):
        minm = mat[0][i]

        for j in range(1, n, 1):
            if (mat[j][i] < minm):
                minm = mat[j][i]
        print(minm, end = ",")
    print("}")
if __name__ == '__main__':
    n = 3
    m = 3
    mat = [[2, 1, 7],
           [3, 7, 2 ],
           [ 5, 4, 9 ]];
    print("Minimum element of each row is", end = " ")
    smallestInRow(mat, n, m)
    print("Minimum element of each column is", end = " ")
    smallestInCol(mat, n, m)