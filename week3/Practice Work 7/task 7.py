import math

x = float(input('x : '))
y = float(input('y : '))
z = float(input('z : '))
t = float(input('t : '))
def Square(x, y, z, t):
     d = math.sqrt(x*x+y*y)
     s1 = x*y*0.5
     g2 = 0.25*math.sqrt((d+z+t)*(d+z-t)*(d+t-z)*(z+t-d))
     return s1 + g2
print(Square(x,y,z,t))