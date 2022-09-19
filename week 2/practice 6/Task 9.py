N = int(input("write N: "))
array = []
min_ = float('inf')
for i in range(N):
    num = float(input(f"enter array[{i}] element: "))
    array.append(num)
    if abs(num) < abs(min_):
        min_ = num
print(f"The minimum modulo number: {min_}")
print("Array in reverse order: ", end=' ')
for i in reversed(range(0, N)):
    print(array[i], end=' ')