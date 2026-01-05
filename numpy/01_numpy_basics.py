import numpy as np

# 1D array
arr = np.array([1, 2, 3, 4, 5])
print("arr:", arr)
print("dtype:", arr.dtype)
print("shape:", arr.shape)

# math
print("mean:", arr.mean())
print("sum:", arr.sum())
print("min/max:", arr.min(), arr.max())

# create arrays
zeros = np.zeros(5)
ones = np.ones(5)
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)

print("zeros:", zeros)
print("ones:", ones)
print("arange:", arange)
print("linspace:", linspace)
