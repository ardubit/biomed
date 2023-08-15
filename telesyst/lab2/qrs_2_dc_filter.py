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
qrs_a_dc_filtered = qrs_a
qrs_a_dc_filtered = np.zeros((T_QRS_complexes, T_QRS_complex))
# print(type(qrs_a_dc_filtered))
# print(type(qrs_a))
# <class 'numpy.ndarray'>

for i in range(len(qrs_a)):
    print('QRS_A (object)' + str(i) + ': \n', qrs_a[i])
    mean = np.mean(qrs_a[i])
    print('Mean in QRS_A: \n', mean)
    for j in range(len(qrs_a[i])):
        qrs_a_dc_filtered[i][j] = qrs_a[i][j] - mean
        print(qrs_a_dc_filtered[i][j])

    # rev 1.0
    # for qrs_complex in qrs_a:
    #     for j in range(len(qrs_complex)):
    #         qrs_a_dc_filtered[i][j] = qrs_complex[j] - mean
    #         # print(qrs_complex[j])
    #         # print(qrs_a_dc_filtered[i][j])

title = 'Сигнал після вилучення Постійної складової. QRS-комплекси А-типу'
plot(t_shifted, qrs_n, limit, step, title, xlabel, ylabel)

title = 'Сигнал після вилучення Постійної складової. QRS-комплекси А-типу'
plot(t_shifted, qrs_n, limit, step, title, xlabel, ylabel)

title = 'Сигнал після вилучення Постійної складової. QRS-комплекси А-типу'
plot(t_shifted, qrs_n, limit, step, title, xlabel, ylabel)