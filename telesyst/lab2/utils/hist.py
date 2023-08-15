import matplotlib.pyplot as plt
import numpy as np

data = np.random.default_rng(123).rayleigh(1, 70)
counts, edges, bars = plt.hist(data)
plt.bar_label(bars)
plt.show()

x1 = (-2, -2, -1, 0, 1, 1, 2, 3, 4, 4, 4, 5, -5)
x2 = (-2, -1, -1, 0, 0, 1, 1, 3, 4, 4, 2, 5, 3)
data = [x1, x2]

# HIST_BINS = np.linspace(-6, 6, 20)
# HIST_BINS = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
HIST_BINS = range(-6, 6)
# HIST_BINS = 'auto'
# histtype='barstacked'
counts, edges, bars = plt.hist(data, HIST_BINS, alpha=0.8, edgecolor='white', label=['x1', 'x2'])
# plt.hist(x2, HIST_BINS, color = 'blue')
plt.title('Гістограма')
plt.xlabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
plt.ylabel('Частота появи ознаки', fontsize=14, fontname="Arial")
plt.grid(True, linestyle='--')
plt.bar_label(bars[0])
plt.bar_label(bars[1])
plt.legend()
plt.show()

# Implementation of matplotlib function
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
    
np.random.seed(10**7)
n_bins = 20
x = np.random.randn(100, 3)
colors = ['orange', 'red', 'green']
plt.hist(x, n_bins, density = True, histtype ='bar', color = colors, label = colors) 
plt.legend(prop ={'size': 10})
plt.title('matplotlib.pyplot.hist() function Example\n\n') 
plt.show()