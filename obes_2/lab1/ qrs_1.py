from matplotlib import pyplot as plt
from scipy.io import loadmat
import numpy as np

# qrs_a = loadmat("A_type.mat")["qrs_a"][0];
qrs_a = loadmat("A_type.mat")["qrs_a"];
FREQ = 257;
T_QRS = qrs_a.shape[0]; # кількість відліків, довжина масиву
T_QRS_complex = len(qrs_a[0]) # 128 відліків у кожному сигналі
t = np.linspace(0, 1 / FREQ * T_QRS, T_QRS_complex);


 # len(qrs_a)
for i in range(10):
    # Перебор кожного комплексу, всього 62
    print(qrs_a[i])

#     fig, axs = plt.subplots(lim)
#     fig.suptitle('Vertically stacked subplots')
#     axs[i].plot(t, qrs_a[i])
# plt.show()

    plt.plot(t, qrs_a[i])
    plt.title('qrs_a, Початковий сигнал, комплекс №:' + str(i), fontname="Arial")
    plt.xlabel('Час, c', fontsize=14, fontname="Arial")
    plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
    plt.grid(True)
plt.show()
