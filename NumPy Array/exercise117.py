import numpy as np


A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 4.99],
              [14.99, 2.39, 7.29]])

print(np.sort(A, axis=1))
print(np.sort(A, axis=0))