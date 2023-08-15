import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image0261.jpg', cv2.IMREAD_GRAYSCALE);
img_noise = cv2.imread('image0261+gray.png', cv2.IMREAD_GRAYSCALE);

for i in ([img,img_noise]):
    dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(i));
    plt.figure();
    plt.subplot(131), plt.imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray') 
    plt.title('Центровані амплітудні спектри'), plt.xticks([]), plt.yticks([]) 
    # Вихідне зображення
    plt.subplot(132), plt.imshow(i, cmap='gray')
    plt.title('Початкове зображення'), plt.xticks([]), plt.yticks([])
    # Обернене перетворення
    plt.subplot(133), plt.imshow(abs(np.fft.ifft2(dark_image_grey_fourier)), cmap='gray')
    plt.title('Відновлене зображення'), plt.xticks([]), plt.yticks([]) 
    plt.show()