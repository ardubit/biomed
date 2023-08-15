import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

# qrs_a = loadmat("A_type.mat")["qrs_a"][0];
qrs_a = loadmat("data/A_type.mat")["qrs_a"]
qrs_n = loadmat("data/N_type.mat")["qrs_n"]
qrs_v = loadmat("data/V_type.mat")["qrs_v"]

FREQ = 257;
T_QRS_complexes = qrs_a.shape[0]; # 62 комплекси
T_QRS_complex = len(qrs_a[0]) # 128 відліків у кожному комплексі (сигналі)

t_qrs = np.linspace(0, 1 / FREQ * T_QRS_complexes, T_QRS_complexes); # 62 комплекси
t = np.linspace(0, 1 / FREQ * T_QRS_complex, T_QRS_complex); # 128 відліків (значень)

SHIFT = 46
t_qrs_shifted = np.linspace(0 - 1/FREQ * SHIFT, 1 / FREQ * (T_QRS_complexes - SHIFT), T_QRS_complexes)
t_shifted = np.linspace(0 - 1/FREQ * SHIFT, 1 / FREQ * (T_QRS_complex - SHIFT), T_QRS_complex)

# debug 
# ===========================
print('Кількість сигналів (QRS-комплексів): ', T_QRS_complexes)
print('Кількість відліків сигналу QRS_A: ', len(qrs_a[0]))
print('Кількість відліків сигналу QRS_N: ', len(qrs_n[0]))
print('Кількість відліків сигналу QRS_V: ', len(qrs_v[0]))
print('QRS_A: ', qrs_a[1]);
print('QRS_A: ', qrs_a[2]);

# Пошук максимального значення, R-піку
# ===========================
print(type(qrs_a));
r_peak = np.max(qrs_a);
print('Максимальне значення піку зі всіх QRS-комплексів типу-A: ', r_peak)
for i in range(len(qrs_a)):
    r_peak = np.max(qrs_a[i])
    peak_index = np.where(qrs_a[i] == r_peak)
    print('Значення піку QRS-A:' + str(i) +'\t', r_peak, '\t індекс:', peak_index)

print(type(qrs_n));
r_peak = np.max(qrs_n);
print('Максимальне значення піку зі всіх QRS-комплексів типу-N: ', r_peak)
for i in range(len(qrs_n)):
    r_peak = np.max(qrs_n[i])
    peak_index = np.where(qrs_n[i] == r_peak)
    print('Значення піку QRS-N:' + str(i) +'\t', r_peak, '\t індекс:', peak_index)

print(type(qrs_v));
r_peak = np.max(qrs_v);
print('Максимальне значення піку зі всіх QRS-комплексів типу-V: ', r_peak)
for i in range(len(qrs_v)):
    r_peak = np.max(qrs_v[i])
    peak_index = np.where(qrs_v[i] == r_peak)
    print('Значення піку QRS-V:' + str(i) +'\t', r_peak, '\t індекс:', peak_index)

# Плот по 7 сигналів
# ===========================
limit = qrs_a.shape[0] # 62
step = 7
figure_ctr = 0

def plot(t, qrs, limit, step, title, xlabel, ylabel):
    global figure_ctr
    start = 0 
    # end не включається
    for end in range(0, limit + step, step):
        # print(end)
        if end == limit + 1:
            # print(end)
            start = end - step; end = limit
        for i in range(start, end):
            plt.plot(t, qrs[i], label=str([i]))
            plt.title(title, fontname="Arial")
            plt.xlabel(xlabel, fontsize=14, fontname="Arial")
            plt.ylabel(ylabel, fontsize=14, fontname="Arial")
            plt.grid(True)
            plt.legend()
        start = end
        # Збереження завжди перед показом
        plt.savefig('test_figures/Figure_' + str(figure_ctr) + '.png', dpi=150)
        plt.show(block=False)
        plt.pause(1)
        plt.close()
        figure_ctr = figure_ctr + 1

''' 
# 7936 Y-відліків (128х62) = 100%
# 100 / 7936 = 0.0126 на кожен відлік

# Повертав 0.33 на кожен відлік, у 3-рази більше
# 7936 * 1 / х = 0.3334
# x = 7936 / 0.3334
# x = 23803

# 7936 * 1 / х = 0.01
# x = 7936 / 0.01
# x = 793600
''' 