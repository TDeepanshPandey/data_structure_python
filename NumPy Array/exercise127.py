import numpy as np


A = np.array([[2, 0],
              [4, 2],
              [5, 3],
              [4, 2]])
B = np.array([[4, 0, 2, 1, 1, 0, 2, 9]])

print(np.dot(A,B.reshape(2, -1)))