import numpy as np

n = 5 # number of coins
counts = np.zeros(n+1, dtype=np.int32)  # each index i number of arrangens is the number of arrangements of i coins
counts[1] = 1
for i in range(2, n+1):
    counts[i] = np.sum(counts[1:i+1] * counts[i:0:-1]) //2
    # TODO: correct indexes,  use only half of the indexes in the sum (symmetry)
print(counts)
