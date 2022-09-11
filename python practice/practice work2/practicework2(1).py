import math
a=int(input("Enter 1st value: ")) 
b=int(input("Enter 2nd value: "))
c=int(input("Enter 3rd value: "))

s = (((a**2 + b)*c) / (2*(a-b)+4))

print("s={0:.2f}".format(s))