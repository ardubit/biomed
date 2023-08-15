import numpy as np

array = np.arange(15).reshape(3, 5);
print("Original array : \n", array);

# numpy.ravel() == numpy.reshape(-1)

array = array.ravel();
print("\nravel() : ", array);