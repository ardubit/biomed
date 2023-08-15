import numpy as np
import matplotlib.pyplot as plt
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, rescale, iradon
import matplotlib.pyplot as plt
from skimage.transform.radon_transform import _get_fourier_filter
from PIL import Image
import time

""" Функція I=iradon(P, theta, interp, filter, d, n) містить опис параметрів, 
які використовуються у оберненому перетворенні. 
Параметр interp визначає тип інтерполяції. 
Список доступних опцій: 
    'nearest' - інтерполяція за найближчим околом; 
    'Linear' - лінійна інтерполяція; 
    'Spline' - сплайнова інтерполяція. 
Параметр filter описує який тип фільтра, який використовується для частотної фільтрації: 
    'Ram-Lak', 'Shepp-Logan', 'Cosine', 'Hamming', 'Hann'.
"""

# 2.0
IMG_SIZE = 725
path = r'no_98.jpg'
image = Image.open(path).convert(mode='L')
image = image.resize((IMG_SIZE, IMG_SIZE), Image.NEAREST)
image = np.asarray(image)

filt = ['ramp','shepp-logan','cosine','hamming','hann']
interp = ['linear','nearest','cubic']

for aa in [1, 2]:
    if (aa == 1): 
        # param = [5, 10, 25, 50, 100]
        param = [180]
    else:
        param = np.linspace(0, 51, 51, endpoint=False)
        sq_err = np.zeros([15, 51])
    b = -1
    for ff in range(len(param)):
        theta = np.linspace(0, 180, (int)(param[ff]), endpoint=False) 
        sinogram = radon(image, theta=theta)
        b = 0
        for i in range(len(filt)):
            if (aa == 1): 
                plt.figure()
                plt.subplot(1, 4, 1)
                a = 2
                plt.imshow(image)
                plt.title('Початкове зображення')
            for j in range(len(interp)):
                reconstruction = iradon(sinogram, theta=theta, filter_name = filt[i],interpolation = interp[j])
                if (aa == 1):
                    plt.subplot(1, 4, a) 
                    a = a + 1
                    plt.imshow(reconstruction)
                    plt.title('Filter: '+str(filt[i])+', inteprolation: '+str(interp[j]));
                else:
                    error = reconstruction - image
                    sq_err[b][ff] = np.sqrt(np.mean(error**2))
                    b = b + 1
        plt.show()

for ii in range(sq_err.shape[0]):
    plt.plot(param, sq_err[ii][:], label=str(ii)+', '+filt[ii//3]+', '+interp[ii%3])
    plt.legend()
    plt.grid()
    plt.xlabel('Кількість використаних проекцій = ')
    plt.ylabel('Середньоквадратичну похибка') 
    plt.show()
