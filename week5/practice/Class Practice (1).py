class Rectangle:
    def __init__(self, color = "green", width = 100, height = 100, lenth = 100):
        self.color = color
        self.width = width
        self.height = height
        self.lenth = lenth
        
    def cub(self):
        return self.width * self.height * self.lenth

    def square(self):
        return self.width * self.height

rectan1 = Rectangle()
print (rectan1.color)
print (rectan1.square())


rectan2 = Rectangle("Puprle", 33, 46)
print (rectan2.color)
print (rectan2.square())

rectan3 = Rectangle("white", 8, 2, 6)
print (rectan3.color)
print (rectan3.square())
print (rectan3.cub())