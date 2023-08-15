# import scipy and numpy
import scipy
import numpy as np

x = np.arange(6)
print(x)

# Using scipy.fftfreq() method
gfg = scipy.fft.fftshift(x)

print(gfg)