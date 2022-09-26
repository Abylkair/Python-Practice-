import math
cat1 = int(input('Enter the first cathet of the first triangle: '))
cat2 = int(input('Enter the second cathet of the second triangle: '))
cat3 = int(input('Enter the third cathet of the third triangle: '))
cat4 = int(input('Enter the forth cathet of the forth triangle: '))
gipot1 = float(math.sqrt(cat1*cat1 + cat2*cat2))

gipot2 = float(math.sqrt(cat3*cat3 + cat4*cat4))

print(gipot1)

if gipot1 > gipot2:

   d1 = gipot1 - gipot2

   print('The hypotenuse of the first triangle is greater than the hypotenuse of the second triangle by: ' + str(d1) + '.\nThe hypotenuse of the first triangle is: ' + str(gipot1) + '.\nThe hypotenuse of the second triangle is: ' + str(gipot2))

else:

   d2 = gipot2 - gipot1

   print('The hypotenuse of the first triangle is greater than the hypotenuse of the second triangle by: ' + str(d2) + '.\nThe hypotenuse of the first triangle is: ' + str(gipot1) + '.\nThe hypotenuse of the second triangle is: ' + str(gipot2))