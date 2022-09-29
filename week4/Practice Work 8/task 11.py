from random import randint
v = 6
matrix = [[randint(-10, 10) for j in range(v)] for i in range(v)]
for row in matrix:
    print(row)
min_ = [min(row) for row in matrix]
ind_row_with_min = min_.index(min(min_))
print(ind_row_with_min)
print('sum: {}'.format(sum(matrix[ind_row_with_min])))