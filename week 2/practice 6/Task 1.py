N = int(input("write N: "))
array = []
min_ = float('inf')
for i in range(N):
    num = float(input(f"write array[{i}] element: "))
    array.append(num)
    if abs(num) < abs(min_):
        min_ = num
print(f"The minimum modulo number: {min_}")
print("Array in reverse order: ", end=' ')
for i in reversed(range(0, N)):
    print(array[i], end=' ')
    
data = [1.2, -5, 0, 3.4, 0, 0]
mean = sum(data) / len(data)
data = [it if it else mean for it in data]