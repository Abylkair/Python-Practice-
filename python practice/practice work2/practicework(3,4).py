import math
x=3
y=5

result = ( math.sqrt(math.fabs(y)) + ((math.atan(math.log(x))**3) / ( (x*y)-y+1) ))
print("result={0:.2f}".format(result))