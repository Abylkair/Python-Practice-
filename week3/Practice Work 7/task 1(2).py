from functools import reduce  # Function for sequence reconciliation
from operator import mul  # A function multiplying 2 numbers
 
list = [16, 15, 9, 14, 13]  # Source list
 
result = reduce(mul, list)
# List for reconciliation
# We use multiplication
# Collapsing the container

print("composition: ", result)
 
result2 = sum(list) / len(list)
print("arithmetic mean: ", result2)
