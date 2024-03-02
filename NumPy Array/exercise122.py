import numpy as np


feature1 = np.array([1.6, 0.9, 2.2])
feature2 = np.array([0.4, 1.3, 3.2])
feature3 = np.array([1.4, 0.3, 1.2])

print(np.column_stack((feature1, feature2, feature3)))