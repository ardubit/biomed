import numpy as np
import matplotlib.pyplot as plt
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, rescale, iradon
import matplotlib.pyplot as plt
from skimage.transform.radon_transform import _get_fourier_filter
from PIL import Image
import cv2

IMG_SIZE = 725

# img = cv2.imread('no_98.jpg')
# image = cv2.resize(img, dsize=(IMG_SIZE, IMG_SIZE), interpolation=cv2.INTER_LINEAR)

# image = shepp_logan_phantom()
# image = rescale(image, scale=0.4, mode='reflect', channel_axis=None)

# 2.0
path = r'no_98.jpg'
image = Image.open(path).convert(mode='L')
image = image.resize((IMG_SIZE, IMG_SIZE), Image.NEAREST)
image = np.asarray(image)

# image = plt.imread(path)
image = rescale(image, scale=0.4, mode='reflect', channel_axis=None)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))
ax1.set_title("Початкове зображення")
ax1.imshow(image, cmap=plt.cm.Greys_r)

theta = np.linspace(0., 180., max(image.shape), endpoint=False)
sinogram = radon(image, theta=theta)
dx, dy = 0.5 * 180.0 / max(image.shape), 0.5 / sinogram.shape[0]
ax2.set_title("Перетворення Радона \n(Sinogram)")
ax2.set_xlabel("Projection angle (deg)")
ax2.set_ylabel("Projection position (pixels)")
ax2.imshow(sinogram, cmap=plt.cm.Greys_r,
           extent=(-dx, 180.0 + dx, -dy, sinogram.shape[0] + dy),
           aspect='auto')
fig.tight_layout()
plt.show()

filters = ['ramp', 'shepp-logan', 'cosine', 'hamming', 'hann']

for ix, f in enumerate(filters):
    response = _get_fourier_filter(2000, f)
    plt.plot(response, label=f)

plt.xlim([0, 1000])
plt.xlabel('frequency')
plt.legend()
plt.show()

reconstruction_fbp = iradon(sinogram, theta=theta, filter_name='ramp')

# print(reconstruction_fbp.shape)
# print(image.shape)

shape = reconstruction_fbp.shape
image = np.resize(image, shape)

print(reconstruction_fbp.shape)
print(image.shape)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5), sharex=True, sharey=True)
ax1.set_title("Відновлене зображення")
ax1.imshow(reconstruction_fbp, cmap=plt.cm.Greys_r)
ax2.set_title("Вихідне зображення")
ax2.imshow(image, cmap=plt.cm.Greys_r)
plt.show()

error = reconstruction_fbp - image
print(f'FBP rms reconstruction error: {np.sqrt(np.mean(error**2)):.3g}')

imkwargs = dict(vmin=-0.2, vmax=0.2)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5),
                               sharex=True, sharey=True)
ax1.set_title("Відновлене зображення")
ax1.imshow(reconstruction_fbp, cmap=plt.cm.Greys_r)
ax2.set_title("Похибка відновлення")
ax2.imshow(reconstruction_fbp - image, cmap=plt.cm.Greys_r, **imkwargs)
plt.show()