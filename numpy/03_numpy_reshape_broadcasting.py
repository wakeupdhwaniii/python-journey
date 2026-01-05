import numpy as np

mat = np.array([[1, 2, 3],
                [4, 5, 6]])

print("mat:\n", mat)
print("shape:", mat.shape)

# reshape
flat = mat.reshape(6,)
print("flat:", flat)

mat2 = flat.reshape(2, 3)
print("mat2:\n", mat2)

# broadcasting
add_row = mat + np.array([10, 20, 30])
print("broadcast add row:\n", add_row)

# elementwise ops
print("mat * 2:\n", mat * 2)
