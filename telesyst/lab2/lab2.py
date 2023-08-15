import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy import signal
import numpy as np
from sklearn import preprocessing

qrs_a = loadmat("A_type.mat")["qrs_a"][0];
qrs_n = loadmat("N_type.mat")["qrs_n"][0];
qrs_v = loadmat("V_type.mat")["qrs_v"][0];
val = loadmat("I22m.mat")["val"][0];

# Опис
# ===========================
# Комплекс N-типу відповідає нормальному циклу роботи серця. 
# Під А-типом розуміється комплекс передчасного скорочення серцевого м'яза.
# V-тип комплекс без R-піку. Забір крові в серці відбувається, а команда на її виштовхування відсутня.
# 
#   1. Початкові сигнали
#   2. Зсув R піку до нуля
#   3. Видалення з сигналів постійної складової
#   4. Нормалізація сигналів
#

#   0. Початкові сигнали
# ===========================
fs = 257;
t_a = qrs_a.shape[0]; # кількість відліків
t_n = qrs_n.shape[0];
t_v = qrs_v.shape[0];
t_val = val.shape[0];

# debug 
# ===========================
print(t_a);
print(len(qrs_a));
print(len(qrs_n));
print(len(qrs_v));
print(len(val));
print('QRS_A: ', qrs_a[1]);
print('QRS_A: ', qrs_a[2]);

# for i in range(qrs_a):
#     i =;

# (start, stop, num)
t = np.linspace(0, 1 / fs * t_a, t_a);
plt.plot(t, qrs_a);
plt.title('A_type.mat, Передсердна екстрасистолія (Atrial premature beats)', fontname="Arial")
plt.xlabel('Час, c', fontsize=14, fontname="Arial")
plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
plt.grid(True);
plt.show();

t = np.linspace(0, 1 / fs * t_n, t_n);
plt.plot(t, qrs_n);
plt.title('N_type.mat, Нормальні серцеві удари (Normal beats)', fontname="Arial")
plt.xlabel('Час, c', fontsize=14, fontname="Arial")
plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
plt.grid(True);
plt.show();

t = np.linspace(0, 1 / fs * t_v, t_v);
plt.plot(t, qrs_v);
plt.title('V_type.mat, Передчасне скорочення шлуночків (Premature ventricular contraction)', fontname="Arial")
plt.xlabel('Час, c', fontsize=14, fontname="Arial")
plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
plt.grid(True);
plt.show();

t = np.linspace(0, 1 / fs * t_val, t_val);
plt.plot(t, val);
plt.title('I22m.mat', fontname="Arial")
plt.xlabel('Час, c', fontsize=14, fontname="Arial")
plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
plt.grid(True);
plt.show();

# Синхронізація за R-зубцем
# ===========================
r_peak = np.max(qrs_a);
print('Пік: ', r_peak);
print(type(qrs_a));
peak_index = np.where(qrs_a == r_peak);
print(peak_index);
qrs_a = qrs_a[peak_index:];

# plt.plot(t, qrs_a);
# plt.title('Синхронізація за R-зубцем, A_type.mat, Передсердна екстрасистолія (Atrial premature beats)', fontname="Arial")
# plt.xlabel('Час, c', fontsize=14, fontname="Arial")
# plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
# plt.grid(True);
# plt.show();

# 1. Видалення з сигналів постійної складової
# ===========================

# Нормалізація сигналів
# ===========================
# normalized_qrs_a = signal.normalize(qrs_a);
qrs_a.reshape(-1, 1);
normalized_qrs_a = preprocessing.normalize(qrs_a);
plt.plot(t, normalized_qrs_a);
plt.title('Нормалізований сигнал A_type.mat, Передсердна екстрасистолія', fontname="Arial")
plt.xlabel('Час, c', fontsize=14, fontname="Arial")
plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
plt.grid(True);
plt.show();



# debug 
# ===========================
# Y = np.array([1, 2, 3, 4, 5]);
# print("Array:", Y);
# print("Output Y.shape[]:", Y.shape, Y);
# for i in range(Y.shape[0]):
#    print(Y[i], end=" ")

# print("\n")

# for i in range(len(Y)):
#    print(Y[i], end=" ")