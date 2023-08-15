import numpy as np
import matplotlib.pyplot as plt
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, rescale, iradon
import matplotlib.pyplot as plt
from skimage.transform.radon_transform import _get_fourier_filter
from PIL import Image
import time

# img = cv2.imread('no_98.jpg')
# image = cv2.resize(img, dsize=(IMG_SIZE, IMG_SIZE), interpolation=cv2.INTER_LINEAR)

# image = shepp_logan_phantom()
# image = rescale(image, scale=0.4, mode='reflect', channel_axis=None)

# 2.0
IMG_SIZE = 725
path = r'no_98.jpg'
image = Image.open(path).convert(mode='L')
image = image.resize((IMG_SIZE, IMG_SIZE), Image.NEAREST)
image = np.asarray(image)

# 1.0
# image = shepp_logan_phantom()
# image = rescale(image, scale=0.4, mode='reflect', channel_axis=None)
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))
# ax1.set_title("Початкове зображення")
# ax1.imshow(image, cmap=plt.cm.Greys_r)
# plt.show()

param = [10, 25, 50, 100, 500, 1000]
print(range(len(param)))
start_time = np.zeros(len(param))
end_time = np.zeros(len(param))

for i in range(len(param)):
    print(i)
    theta = np.linspace(0, 180, param[i], endpoint=False)
    sinogram = radon(image, theta=theta)
    start_time[i] = time.time()
    reconstruction = iradon(sinogram, theta=theta)
    end_time[i] = time.time()
    print('Done!\n')
    
    # Створює сітку 2х3 та друкує кожне зображення у сублот "i"
    plt.subplot(2, 3, i+1)
    plt.title('Кількість використаних проекцій = ' + str(param[i]))
    plt.imshow(reconstruction)
plt.show()

plt.figure()
# Залежність часу відновлення зображення від кількості використаних проекцій
# param = np.linspace(0, 201, 201, endpoint=False);
plt.plot(param, 1e3*(end_time - start_time))
plt.grid()
plt.xlabel('Кількість проекцій')
plt.ylabel('Час, ms')
plt.show()

