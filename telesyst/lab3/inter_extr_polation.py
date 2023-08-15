from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy import interpolate

x = np.array([25, 60, 70, 100, 125]).reshape((-1, 1))
y = np.array([90, 100 , 110, 125, 140])

'''
import numpy as np
from scipy import interpolate

x = np.arange(0,10)
y = np.exp(-x/3.0)
f = interpolate.interp1d(x, y, fill_value='extrapolate')

print f(9)
print f(11)
'''

# SciPy extrapolation
import numpy as np

x = np.array([25, 60, 70, 100, 125])
y = np.array([90, 100 , 110, 125, 140])

f = interpolate.interp1d(x, y, fill_value='extrapolate')

print(f(125))
print(f(25))

# SciPy extrapolation
from scipy import interpolate

# х
w_load = np.array([25, 60, 70, 100, 125]).reshape((-1, 1))
# y
f_heart_beats = np.array([90, 100 , 110, 125, 140])

# Reshape back to the initial 1D shape "Flattening the arrays"
x = w_load.reshape(-1)
y = f_heart_beats

f = interpolate.interp1d(x, y, fill_value='extrapolate')

x = np.linspace(0, 240, 20)
y = f(x)

plt.plot(x, y)
plt.show()