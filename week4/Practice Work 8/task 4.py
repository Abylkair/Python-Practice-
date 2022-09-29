import random
b=[]
for i in range(len("matrix")):
    b.append(sum("matrix", [i]))
print('matrix', [b.index(max(b))],max(b),'matrix' ,[b.index(min(b))],min(b))
