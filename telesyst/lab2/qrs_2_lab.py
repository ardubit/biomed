from matplotlib import pyplot as plt
from scipy.io import loadmat
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing

# Дані та функції виводу
from qrs_2_plot import *

DEBUG = 'On'
# DEBUG = ''
# DEBUG_HIST = 'On'
DEBUG_HIST = ''

# 2. Зсув R-піку до нуля
# ===========================
SHIFT = 46
t_qrs_shifted = np.linspace(0 - 1/FREQ * SHIFT, 1 / FREQ * (T_QRS_complexes - SHIFT), T_QRS_complexes)
t_shifted = np.linspace(0 - 1/FREQ * SHIFT, 1 / FREQ * (T_QRS_complex - SHIFT), T_QRS_complex)
# LIMIT = range(52, 62)

if (DEBUG != 'On'):
    title = 'qrs_a, Початкові сигнали, центрований R-пік. QRS-комплекси А-типу'
    xlabel = 'Час, c'
    ylabel = 'Амплітуда, мВ'
    plot(t_shifted, qrs_a, limit, step, title, xlabel, ylabel)

    title = 'qrs_n, Початкові сигнали, центрований R-пік. QRS-комплекси N-типу'
    plot(t_shifted, qrs_n, limit, step, title, xlabel, ylabel)

    title = 'qrs_v, Початкові сигнали, центрований R-пік. QRS-комплекси V-типу'
    plot(t_shifted, qrs_v, limit, step, title, xlabel, ylabel)

# qrs = [qrs_a, qrs_n, qrs_v]
# titles = ['A-типу','N-типу','V-типу']
# for q in range(len(qrs)):
#     for i in range(LIMIT):
#         plt.plot(t_shifted, qrs[q][i], label=str([i]))
#         plt.title('Початкові сигнали, центрований R-пік. QRS-комплекси ' + titles[q], fontname="Arial")
#         # plt.title('qrs_a, Початковий сигнал, комплекс №:' + str(i), fontname="Arial")
#         plt.xlabel('Час, c', fontsize=14, fontname="Arial")
#         plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
#         plt.grid(True)
#     plt.show()

# 3. Вилучення постійної складової з сигналу кожного комплексу
# ===========================
''' 
    QRS_A 62x128
    =====================================
    Комплекс [0] ->  data [0], [1], [2] ... [127]
    Комплекс [1] ->  data [0], [1], [2] ... [127]
    Комплекс [2] ->  data [0], [1], [2] ... [127]
    ...
    Комплекс [61]
'''
# Debug
i = 0; j = 2
print('QRS: [i],[j]' + str(i) + ',' + str(j) + ' ', qrs_a[i][j])

# Обирається один комплекс як об'єкт з 62-х комплексів та визначається 
# середнє значення з обраного кожного комплексу
# ======
# print(len(qrs_a))
# # 62
# print(len(qrs_complex))
# # 128
# print(range(len(qrs_a)))
# # 0, 62
# print(range(len(qrs_complex)))
# # 0, 128

# Копія комплексу
qrs_a_dc_filtered = qrs_a.copy()
qrs_n_dc_filtered = qrs_n.copy()
qrs_v_dc_filtered = qrs_v.copy()
qrs_a_dc_filtered = np.zeros((T_QRS_complexes, T_QRS_complex))
qrs_n_dc_filtered = np.zeros((T_QRS_complexes, T_QRS_complex))
qrs_v_dc_filtered = np.zeros((T_QRS_complexes, T_QRS_complex))
# print(type(qrs_a_dc_filtered))
# print(type(qrs_a))
# <class 'numpy.ndarray'>

# Вхід комплекс, вихідний фільрований комплекс
def dc_filtered(qrs, qrs_dc_filtered):
    for i in range(len(qrs)):
        print('QRS_A (object)' + str(i) + ': \n', qrs[i])
        mean = np.mean(qrs[i])
        print('Mean in QRS_A: \n', mean)
        for j in range(len(qrs[i])):
            qrs_dc_filtered[i][j] = qrs[i][j] - mean
            print(qrs_dc_filtered[i][j])

    # rev 1.0
    # for qrs_complex in qrs_a:
    #     for j in range(len(qrs_complex)):
    #         qrs_a_dc_filtered[i][j] = qrs_complex[j] - mean
    #         # print(qrs_complex[j])
    #         # print(qrs_a_dc_filtered[i][j])

dc_filtered(qrs_a, qrs_a_dc_filtered)
dc_filtered(qrs_n, qrs_n_dc_filtered)
dc_filtered(qrs_v, qrs_v_dc_filtered)

if (DEBUG != 'On'):
    title = 'Сигнал після вилучення Постійної складової. QRS-комплекси А-типу'
    plot(t_shifted, qrs_a_dc_filtered, limit, step, title, xlabel, ylabel)

    title = 'Сигнал після вилучення Постійної складової. QRS-комплекси N-типу'
    plot(t_shifted, qrs_n_dc_filtered, limit, step, title, xlabel, ylabel)

    title = 'Сигнал після вилучення Постійної складової. QRS-комплекси V-типу'
    plot(t_shifted, qrs_v_dc_filtered, limit, step, title, xlabel, ylabel)

# 4. Нормалізація
# ===========================
# scaler = preprocessing.MinMaxScaler()
# qrs_a_normalized = scaler.fit_transform(qrs_a_dc_filtered);

qrs_a_normalized = qrs_a_dc_filtered.copy()
qrs_n_normalized = qrs_n_dc_filtered.copy()
qrs_v_normalized = qrs_v_dc_filtered.copy()
qrs_a_normalized = np.zeros((T_QRS_complexes, T_QRS_complex))
qrs_n_normalized = np.zeros((T_QRS_complexes, T_QRS_complex))
qrs_v_normalized = np.zeros((T_QRS_complexes, T_QRS_complex))

def normaliation(qrs_dc_filtered, qrs_normalized):
    # 1.0
    from numpy.linalg import norm
    for i in range(len(qrs_dc_filtered)):
        print('QRS_A (object)' + str(i) + ': \n', qrs_dc_filtered[i])
        l2 = norm(qrs_dc_filtered[i], ord=2)
        print('L2 QRS_A: \n', l2)
        for j in range(len(qrs_dc_filtered[i])):
            qrs_normalized[i][j] = qrs_dc_filtered[i][j]/l2
            print(qrs_normalized[i][j])

    # 2.0
    # from sklearn.preprocessing import normalize
    # for i in range(len(qrs_a_dc_filtered)):
    #     print('QRS_A (object)' + str(i) + ': \n', qrs_a_dc_filtered[i])
    #     l2 = normalize(qrs_a_dc_filtered[i].reshape(1,-1), norm='l2', axis=1, copy=True,)
    #     print(type(l2))
    #     print('L2 QRS_A: \n', l2)
    #     qrs_a_normalized[i] = qrs_a_dc_filtered[i]/l2
    #     print('L2 Normalazed QRS_A: \n', qrs_a_normalized[i])

normaliation(qrs_a_dc_filtered, qrs_a_normalized)
normaliation(qrs_n_dc_filtered, qrs_n_normalized)
normaliation(qrs_v_dc_filtered, qrs_v_normalized)

if (DEBUG != 'On'):
    title = 'Нормалізований сигнал. QRS-комплекси А-типу'
    plot(t_shifted, qrs_a_normalized, limit, step, title, xlabel, ylabel)

    title = 'Нормалізований сигнал. QRS-комплекси N-типу'
    plot(t_shifted, qrs_n_normalized, limit, step, title, xlabel, ylabel)

    title = 'Нормалізований сигнал. QRS-комплекси V-типу'
    plot(t_shifted, qrs_v_normalized, limit, step, title, xlabel, ylabel)

# 5. Визначення середнього значення відліків QRS-комплексів
# ===========================

qrs_a_mean = np.mean(qrs_a_normalized, axis=0)
qrs_n_mean = np.mean(qrs_n_normalized, axis=0)
qrs_v_mean = np.mean(qrs_v_normalized, axis=0)
qrs_mean = [qrs_a_mean, qrs_n_mean, qrs_v_mean]
print('Mean is done!')

if (DEBUG != 'On'):
    titles = ['A-типу','N-типу','V-типу']
    for i in range(3):
        plt.plot(t_shifted, qrs_mean[i], label=str(titles[i]))
        plt.title('Усереднений сигнал, QRS-комплекс ' + titles[i], fontname="Arial")
        plt.xlabel('Час, c', fontsize=14, fontname="Arial")
        plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
        plt.grid(True)
        plt.legend()
        # Збереження завжди перед показом
        plt.savefig('test_figures/Figure_Mean_' + str(i) + '.png', dpi=150)
        plt.show()

# 6. Гістограми оцінки інформативності QRS-комплексів
# ===========================

qrs_normalized = np.array([qrs_a_normalized.reshape(-1), 
                  qrs_n_normalized.reshape(-1), 
                  qrs_v_normalized.reshape(-1)])
qrs_normalized = qrs_normalized.tolist()

# 2.1
# ===========================
from matplotlib.ticker import PercentFormatter

BINS = 40
HIST_BINS = np.linspace(-0.6, 0.6, BINS, retstep=True)
PRECISION_FLOATS = 1
HIST_METRIC = np.round(HIST_BINS[1], 2)
labels = ['QRS: A-типу (Atrial beats)', 'QRS: N-типу (Normal beats)', 'QRS: V-типу (Premature ventricular cortraction)']

''' 
#  qrs_normalized
   --------------------------
   qrs_a -- inline after reshape 7936 value
   qrs_n -- inline after reshape 7936 value
   qrs_v -- inline after reshape 7936 value

   # 3 * 7936 = 23808
   print('len(qrs_normalized): ', len(qrs_normalized))
   >>>3
   АЛЕ !!! np.ones_like(qrs_normalized)*100 / len(qrs_normalized) 
   повертає len(qrs_normalized) як 3 * 7936 = 23808 відліків !!!

   np.ones_like returns the same data
   --------------------------
   [0:3]
   -- 7936 value
   -- 7936 value
   -- 7936 value
''' 

# w1 = np.ones_like(qrs_normalized)*100 / len(qrs_normalized)
# w2 = np.ones_like(qrs_normalized)*100 / len(qrs_normalized)
# w3 = np.ones_like(qrs_normalized)*100 / len(qrs_normalized)
# weights = np.array([w1, w2, w3])
# print(np.ones_like(qrs_normalized) / 10)
qrs_len = len(qrs_normalized)
print(qrs_len)

# w = np.ones_like(qrs_normalized) / (len(qrs_normalized) / 3.0 * 100)
w = np.ones_like(qrs_normalized) * 100 / (T_QRS_complexes * T_QRS_complex)
weights = w.tolist()

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111)
counts, edges, bars = plt.hist(qrs_normalized, HIST_BINS[0],
                            alpha=0.8, 
                            edgecolor='white', 
                            label=labels, 
                            density=False,
                            stacked=False,
                            weights=weights
                            )
ax.yaxis.set_major_formatter(PercentFormatter())
plt.title('Гістограма оцінки інформативності елементів QRS-комплексів. Діапазон ознакu, мВ: ' 
          + str(HIST_METRIC) + ', Сітка, (bins): ' + str(BINS), fontsize=14)
plt.xlabel('Значення характерстики форми: Амплітуда, мВ', fontsize=14, fontname="Arial")
plt.ylabel('Відносна частота появи ознаки, %', fontsize=14, fontname="Arial")
plt.grid(True, linestyle='--')

qrs_bars = counts.copy()
for i in range(len(qrs_bars)):
    qrs_bars[i] = np.round(qrs_bars[i], PRECISION_FLOATS)
    plt.bar_label(bars[i], qrs_bars[i], fontsize=6, fontweight='bold')

# plt.bar_label(bars[0], fontsize=8, fontweight='bold')
# plt.bar_label(bars[1], fontsize=8, fontweight='bold')
# plt.bar_label(bars[2], fontsize=8, fontweight='bold')

plt.legend()
if (DEBUG_HIST != 'On'):
    # Збереження завжди перед показом
    plt.savefig('hist_figures/Hist_' + str(BINS) + '.png', dpi=150, bbox_inches = 'tight')
plt.show()


# 2.0
# =======================
# from matplotlib.ticker import PercentFormatter

# HIST_BINS = np.linspace(-0.6, 0.6, 20)
# PRECISION_BARS = 0
# labels = ['QRS: A-типу (Atrial beats)', 'QRS: N-типу (Normal beats)', 'QRS: V-типу (Premature ventricular cortraction)']

# qrs_a_normalized = qrs_a_normalized.flatten()
# weights = np.ones_like(qrs_a_normalized)*100 / len(qrs_a_normalized)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# counts, edges, bars = ax.hist(qrs_a_normalized, HIST_BINS,
#                                alpha=0.8, 
#                                edgecolor='white', 
#                                label=labels, 
#                                density=False,
#                                weights=weights)
# ax.yaxis.set_major_formatter(PercentFormatter())
# plt.title('Гістограма оцінки інформативності елементів QRS-комплексів')
# plt.xlabel('Значення характерстики форми: Амплітуда, мВ', fontsize=14, fontname="Arial")
# plt.ylabel('Відносна частота появи ознаки, %:', fontsize=14, fontname="Arial")
# plt.grid(True, linestyle='--')

# qrs_bars = counts.copy()
# qrs_bars = np.round(qrs_bars, PRECISION_BARS)

# plt.bar_label(bars, qrs_bars, fontsize=8, fontweight='bold')
# # plt.bar_label(bars[0], fontsize=8, fontweight='bold')
# # plt.bar_label(bars[1], fontsize=8, fontweight='bold')
# # plt.bar_label(bars[2], fontsize=8, fontweight='bold')
# plt.legend()
# plt.show()


# 1.0
# =======================
# labels = ['QRS: A-типу (Atrial beats)', 'QRS: N-типу (Normal beats)', 'QRS: V-типу (Premature ventricular cortraction)']
# HIST_BINS = np.linspace(-0.6, 0.6, 20)

# counts, edges, bars, = plt.hist(qrs_normalized, HIST_BINS,
#                                alpha=0.8, 
#                                edgecolor='white', 
#                                label=labels, 
#                                density=False)
# plt.title('Гістограма оцінки інформативності елементів QRS-комплексів')
# plt.xlabel('Значення характерстики форми: Амплітуда, мВ', fontsize=14, fontname="Arial")
# plt.ylabel('Частота появи ознаки:', fontsize=14, fontname="Arial")
# plt.grid(True, linestyle='--')
# plt.bar_label(bars[0], fontsize=8, fontweight='bold')
# plt.bar_label(bars[1], fontsize=8, fontweight='bold')
# plt.bar_label(bars[2], fontsize=8, fontweight='bold')
# plt.legend()
# plt.show()
