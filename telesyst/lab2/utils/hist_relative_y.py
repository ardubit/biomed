import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

#define data values
d1 = np.array([[1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5]])

d2 = np.array([[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1]])

d3 = np.array([[1, 2, 3, 4, 5],
              [1, 2, 3, 5, 5],
              [1, 2, 5, 5, 5]])

# flatten into a 1D array
d1 = d1.reshape(-1)
d2 = d2.reshape(-1)
d3 = d3.reshape(-1)

# list
# data = [d1, d2, d3]

                                        # convert to numpy array 
                                        # data = np.array(data)

                                        # flatten into a 1D array
                                        # data = data.reshape(-1)
                                        # data = data.flatten()

                                        # know shape of the data
                                        # print(data.shape)

data = np.array([d1, d2, d3])
data = data.tolist()

fig = plt.figure()
ax = fig.add_subplot(111)

# weights = [1/len(data)] * len(data)
# 15 шт по 100 і кожне поділи на 15. Тобто 1 відлік 6,66
w1 = np.ones_like(d1)*100 / len(d1)
w2 = np.ones_like(d2)*100 / len(d2)
w3 = np.ones_like(d3)*100 / len(d3)
print(np.ones_like(d1)*100 / len(d1))

# w = np.ones((3, 15))
w = np.array([w1, w2, w3])
w = w.tolist()

# bins - сітка по Х
(n, bins, patches) = plt.hist(data, edgecolor='black', weights=w)

ax.yaxis.set_major_formatter(PercentFormatter())
# for i in range(3):
    # plt.bar_label(patches[i], fontsize=8, fontweight='bold')
    # plt.legend()

plt.show()