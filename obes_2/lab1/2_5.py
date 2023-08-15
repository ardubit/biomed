import numpy as np
import cv2
from matplotlib import pyplot as plt

# Читання початкового зображення з файлу
img = cv2.imread('image0261.jpg')

# Перетворення початкового зображення з одного колірного простору в інший (сірошкальне зображення)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Обчислення двовимірного дискретного перетворення Фур’є
dft = np.fft.fft2(img)

# Зсув нульової частотної складової до центру спектра
dft_shift = np.fft.fftshift(dft)

spec = np.log(abs(dft_shift))
# spec = np.angle(dft_shift)

# Побудова та вивід спектру
plt.figure()
plt.subplot(1,2,1)
plt.title('Input Image')
plt.imshow(img, cmap='gray')

plt.subplot(1,2,2)
plt.title('Spectrum')
plt.imshow((spec), cmap='gray');
plt.show()





