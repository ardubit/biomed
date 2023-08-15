import numpy as np
import matplotlib.pyplot as plt

# Return a copy of the array collapsed into one dimension.
a = np.array([[1,2], [3,4]])
print(a)

a.flatten()
print(a)
# array([1, 2, 3, 4])

a.flatten('F')
# array([1, 3, 2, 4])
print(a)