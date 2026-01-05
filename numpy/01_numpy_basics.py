import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean:", arr.mean())

mat = np.array([[1, 2], [3, 4]])
print("Matrix:\n", mat)
print("Transpose:\n", mat.T)

# Boolean masking
print("Values > 2:", arr[arr > 2])
