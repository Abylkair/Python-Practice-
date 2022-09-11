import math
x=3

y=0.2
result = ( ((5*x*y)/((x**3) -4)) + math.exp(x**2) + math.sqrt( (math.cos(y))**2 - y**2 ))

print("result={0:.2f}".format(result))