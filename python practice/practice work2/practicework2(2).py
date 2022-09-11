import math
x=int(input("Enter 1st value: ")) 
y=int(input("Enter 2nd value: "))

c = (math.sqrt( math.cos(2*y) + math.sin(4*y) + math.sqrt(math.e**x + math.e**(-x))) / ( ((math.e**-x + math.e**x)**3) + (math.sin(4*y) + math.cos(2*y) -2)**2  )   )

print("H={0:.2f}".format(c))
