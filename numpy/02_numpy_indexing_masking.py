import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("first:", arr[0])
print("slice:", arr[1:4])

# boolean masking
mask = arr > 25
print("mask:", mask)
print("values > 25:", arr[mask])

# update using mask
arr[arr > 25] = 999
print("updated:", arr)
