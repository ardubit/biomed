from matplotlib import pyplot as plt
from scipy.io import loadmat
import numpy as np

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

# qrs_a = loadmat("A_type.mat")["qrs_a"][0];
qrs_a = loadmat("data/A_type.mat")["qrs_a"]
qrs_n = loadmat("data/N_type.mat")["qrs_n"]
qrs_v = loadmat("data/V_type.mat")["qrs_v"]

FREQ = 257;
T_QRS = qrs_a.shape[0]; # 62 комплекси
T_QRS_complex = len(qrs_a[0]) # 128 відліків у кожному сигналі
t = np.linspace(0, 1 / FREQ * T_QRS_complex, T_QRS_complex)

LIMIT = 10
for i in range(LIMIT):
    # Перебор кожного комплексу (всього 62)
    print(qrs_a[i])

    plt.plot(t, qrs_a[i])
    plt.title('qrs_a, Початкові сигнали. QRS-комплекси A-типу', fontname="Arial")
    # plt.title('qrs_a, Початковий сигнал, комплекс №:' + str(i), fontname="Arial")
    plt.xlabel('Час, c', fontsize=14, fontname="Arial")
    plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
    plt.grid(True)
plt.show()

for i in range(LIMIT):
    # Перебор кожного комплексу (всього 62)
    print(qrs_n[i])

    plt.plot(t, qrs_n[i])
    plt.title('qrs_n, Початкові сигнали. QRS-комплекси N-типу', fontname="Arial")
    # plt.title('qrs_n, Початковий сигнал, комплекс №:' + str(i), fontname="Arial")
    plt.xlabel('Час, c', fontsize=14, fontname="Arial")
    plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
    plt.grid(True)
plt.show()

for i in range(LIMIT):
    # Перебор кожного комплексу (всього 62)
    print(qrs_v[i])

    plt.plot(t, qrs_v[i])
    plt.title('qrs_v, Початкові сигнали. QRS-комплекси V-типу', fontname="Arial")
    # plt.title('qrs_v, Початковий сигнал, комплекс №:' + str(i), fontname="Arial")
    plt.xlabel('Час, c', fontsize=14, fontname="Arial")
    plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
    plt.grid(True)
plt.show()
