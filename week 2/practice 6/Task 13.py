mass = [0, 1, 1, 10, 2, 4, 2, 10, 0, 2, 2, 6, 8, 9, 9, 9, 0]
print(mass)
mass_num = []
k = 0
for i in range(len(mass) - 1):
    if mass[i] not in mass_num:
        if mass.count(mass[i]) > 1:
            mass_num.append(mass[i])
k = mass.index(mass[i])
print('число =', mass[i], 'индексы =', k, end=' ')
for j in range(mass.count(mass[i]) - 1):
k = mass.index(mass[i], k + 1)
print(k, end=' ')
print()

mass = [10, 1, 11, 12, 30, 14, 20, 15]

print(mass)

for i in range(len(mass)):

   if mass[i] < 15:

       mass[i] *= 2

print(mass)