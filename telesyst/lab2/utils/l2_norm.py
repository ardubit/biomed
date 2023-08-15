import numpy as np
from sklearn.preprocessing import normalize
from scipy import stats

data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(data)
data.reshape(-1, 1)
print(data)
l2 = normalize(data, norm='l2')
print(l2)