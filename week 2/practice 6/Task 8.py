data = [1.2, -5, 0, 3.4, 0, 0]
mean = sum(data) / len(data)
data = [it if it else mean for it in data]
