import datetime
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

plt.plot(x, y)
plt.title('title', fontname="Arial")
plt.xlabel('xlabel', fontsize=14, fontname="Arial")
plt.ylabel('ylabel', fontsize=14, fontname="Arial")
plt.grid(True)
plt.legend()
# fig = plt.gcf()
plt.savefig('test_figures/test_plot.png', dpi=150)
plt.show()
