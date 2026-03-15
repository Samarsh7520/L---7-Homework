import numpy as np

matx = np.arange(9, dtype=np.float64).reshape(3, 3)
print("Matrix:")
print(matx)

arrA = np.array([5, 5, 5])
print("\nArray:", arrA)

print("\nElementwise operations are as:")

print("\nAddition:")
print(np.add(matx, arrA))

print("\nSubtraction:")
print(np.subtract(matx, arrA))

print("\nMultiplication:")
print(np.multiply(matx, arrA))

print("\nDivision:")
print(np.divide(matx, arrA))