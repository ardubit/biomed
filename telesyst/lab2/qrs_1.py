from matplotlib import pyplot as plt
from scipy.io import loadmat
from scipy import signal
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing

# 1. Початкові дані
qrs_a = loadmat("data/A_type.mat")["qrs_a"];
FREQ = 257;
T_QRS = qrs_a.shape[0]; # кількість відліків, довжина масиву
print(T_QRS);
print(len(qrs_a));

t = np.linspace(0, 1 / FREQ * T_QRS, T_QRS);
plt.plot(t, qrs_a);
plt.title('A_type.mat, Передсердна екстрасистолія (Atrial premature beats)', fontname="Arial")
plt.xlabel('Час, c', fontsize=14, fontname="Arial")
plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
plt.grid(True);
plt.show();


