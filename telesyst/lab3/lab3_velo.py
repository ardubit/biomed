from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# х
w_load = np.array([25, 60, 70, 100, 125]).reshape((-1, 1))
# y
f_heart_beats = np.array([90, 100 , 110, 125, 140])
label = ['', '', '']

PAUSE_BEFORE_CLOSE = 3
global figure_ctr
figure_ctr = 0

model = LinearRegression()
# Визначення коеф. лінійної функції
model.fit(w_load, f_heart_beats)
# Обрахунок цсс (y від х)
f_heart_beats_y_pred = model.predict(w_load)

# debug, coefficients: y = m*x + c
r_sq = model.score(w_load, f_heart_beats)
print(f"coefficient of determination: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")
print(model.score(w_load, f_heart_beats))

# Визначення максимального (граничного великого) значення ЧСС
age = 22
f_heart_beats_max_patient = 220 - age

# Визначення максимальної потужності фізичного навантаження
# 1.0
# ==============
for i in range(3):
    plt.title('Оцінка ЧСС f в сталих режимах при різних навантаженнях w', fontname="Arial")
    plt.xlabel('Навантаження, Вт (w):', fontsize=14, fontname="Arial")
    plt.ylabel('ЧСС, уд/хв (f):', fontsize=14, fontname="Arial")
    plt.plot(w_load, f_heart_beats, 'o', label='veloergometr 25-60-75-100-125')
    plt.plot(w_load, f_heart_beats_y_pred)

    if (i == 1 or i == 2):
        plt.axhline(y = f_heart_beats_max_patient, 
                    label='Максимальне значення ЧСС, Вік пацієнта: ' + str(age), 
                    linestyle='dashed', color='b')
    
    if i == 2:
        extrapolated_data = [260]
        w_load = np.append(w_load, extrapolated_data).reshape((-1, 1))
        f_heart_beats_y_pred = model.predict(w_load)
        plt.plot(w_load, f_heart_beats_y_pred, label='extrapolated_data')

    plt.grid(True)
    plt.legend(loc = 'lower right');

    plt.savefig('figures/Figure_' + str(figure_ctr) + '.png', dpi=150)
    plt.show(block=False)
    plt.pause(PAUSE_BEFORE_CLOSE)
    plt.close()
    figure_ctr = figure_ctr + 1




