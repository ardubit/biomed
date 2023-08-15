qrs_a_dc_removed = [[],[]]
for qrs_complex in qrs_a:
    print('QRS_A:', qrs_complex)
    mean = np.mean(qrs_complex)
    
    for i in range(len(qrs_complex)):
        qrs_a_dc_removed.append(i ,i - mean)

    # qrs_a_dc_removed.append(qrs_a - np.mean(signal)) 
    # qrs_a_dcFiltered = qrs_a - np.mean(qrs_a)


    for qrs_complex in qrs_a:
        for j in range(len(qrs_complex)):
            qrs_a_dc_filtered[i][j] = qrs_complex[j] - mean
            print(qrs_complex[j])
            # print(qrs_a_dc_filtered[i][j])

LIMIT = 10
for p in LIMIT:
    for i in range(len(LIMIT)):
        # Перебор кожного комплексу (всього 62)
        print(qrs_a[i])
        plt.plot(t_shifted, qrs_a[i], label=str([i]))
        plt.title('qrs_a, Початкові сигнали, центрований R-пік. QRS-комплекси A-тип', fontname="Arial")
        plt.xlabel('Час, c', fontsize=14, fontname="Arial")
        plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
        plt.grid(True)
        plt.legend();
    plt.show()
    LIMIT = LIMIT + 10

for i in LIMIT:
    # Перебор кожного комплексу (всього 62)
    print(qrs_n[i])
    plt.plot(t_shifted, qrs_n[i], label=str([i]))
    plt.title('qrs_a, Початкові сигнали, центрований R-пік. QRS-комплекси N-тип', fontname="Arial")
    plt.xlabel('Час, c', fontsize=14, fontname="Arial")
    plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
    plt.grid(True)
    plt.legend();
plt.show()

for i in LIMIT:
    # Перебор кожного комплексу (всього 62)
    print(qrs_v[i])
    plt.plot(t_shifted, qrs_v[i], label=str([i]))
    plt.title('qrs_a, Початкові сигнали, центрований R-пік. QRS-комплекси V-тип', fontname="Arial")
    plt.xlabel('Час, c', fontsize=14, fontname="Arial")
    plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
    plt.grid(True)
    plt.legend();
plt.show()

for i in LIMIT:
    # plt.figure()
    plt.subplot(121), plt.plot(t_shifted, qrs_a[i], label=str([i]));
    plt.title('A_type.mat, Початковий сигнал (Atrial premature beats)', fontname="Arial")
    plt.xlabel('Час, c', fontsize=14, fontname="Arial")
    plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
    plt.grid(True)
    plt.legend();

    plt.subplot(122), plt.plot(t_shifted, qrs_a_dc_filtered[i], label=str([i]))
    plt.title('A_type.mat, Сигнал без постійної складової (Atrial premature beats)', fontname="Arial")
    plt.xlabel('Час, c', fontsize=14, fontname="Arial")
    plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
    plt.grid(True)
    plt.legend();
plt.show()

# print('DEBUG')

# plt.figure();
# plt.subplot(121), plt.plot(t_qrs_shifted, qrs_a);
# plt.title('A_type.mat, Початковий сигнал (Atrial premature beats)', fontname="Arial")
# plt.xlabel('Час, c', fontsize=14, fontname="Arial")
# plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
# plt.grid(True);
# plt.subplot(122), plt.plot(t_qrs_shifted, qrs_a_dc_filtered);
# plt.title('A_type.mat, Сигнал без постійної складової (Atrial premature beats)', fontname="Arial")
# plt.xlabel('Час, c', fontsize=14, fontname="Arial")
# plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
# plt.grid(True);
# plt.show();

for i in LIMIT:
# plt.figure();
    plt.subplot(121)
    plt.plot(t_shifted, qrs_a_dc_filtered[i], label=str([i]))
    plt.title('A_type.mat, Сигнал без постійної складової (Atrial premature beats)', fontname="Arial")
    plt.xlabel('Час, c', fontsize=14, fontname="Arial")
    plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
    plt.grid(True);
    plt.legend();

    plt.subplot(122)
    plt.plot(t_shifted, qrs_a_normalized[i], label=str([i]));
    plt.title('A_type.mat, Нормалізований сигнал (Atrial premature beats)', fontname="Arial")
    plt.xlabel('Час, c', fontsize=14, fontname="Arial")
    plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
    plt.grid(True);
    plt.legend();
plt.show();

# 2. Видалення постійної складової
# qrs_a_dc_removed = []
# for signal in qrs_a:
#     qrs_a_dc_removed.append(signal - np.mean(signal))

# qrs_a_dcFiltered = qrs_a - np.mean(qrs_a);

plt.close();
plt.figure();
plt.subplot(121), plt.plot(t, qrs_a);
plt.title('A_type.mat, Початковий сигнал (Atrial premature beats)', fontname="Arial")
plt.xlabel('Час, c', fontsize=14, fontname="Arial")
plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
plt.grid(True);
plt.subplot(122), plt.plot(t, qrs_a_dc_removed);
plt.title('A_type.mat, Сигнал без постійної складової (Atrial premature beats)', fontname="Arial")
plt.xlabel('Час, c', fontsize=14, fontname="Arial")
plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
plt.grid(True);
plt.show();

# qrs_a_normalized = preprocessing.normalize(qrs_a_dc_removed);

scaler = MinMaxScaler();
qrs_a_normalized = scaler.fit_transform(qrs_a_dc_removed);

plt.figure();
plt.plot(t, qrs_a_normalized);
plt.title('A_type.mat, Нормалізований сигнал (Atrial premature beats)', fontname="Arial")
plt.xlabel('Час, c', fontsize=14, fontname="Arial")
plt.ylabel('Амплітуда, мВ', fontsize=14, fontname="Arial")
plt.grid(True);
plt.show();