#Practice 2- Math Operation in Python 
import math 
x = int(input("Enter x: ")) 
y = int(input("Enter y: "))
a = math.sqrt(math.cos(2*y)+math.sin(4*y) + math.sqrt(math.pow(math.e,x) + math.pow(math.e,(-x))))
b = math.pow(((math.pow(math.e,(-x))) + math.pow(math.e,x)),3) * math.pow((math.sin(4*y) + math.cos(2*y) - 2), 2)
c = a/b
print ('Second task answer: ' + str(c))
a=int(input("Enter first value: ")) 
b=int(input("Enter second value: "))
h=int(input("Enter third value: "))

e = (((a**2 + b)*h) / (2*(a-b)+4))

print("s={0:.2f}".format(e))