import numpy as np
import matplotlib.pyplot as plt
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, rescale
from skimage import color
from skimage import io
from PIL import Image

# image = shepp_logan_phantom()
# image = rescale(image, scale=0.4, mode='reflect', channel_axis=None)

# 2.0
path = r'no_98.jpg'
# path = r'cat.jpeg'

# image = plt.imread(path)
# image = rescale(image, scale=0.4, mode='reflect', channel_axis=None)
image = Image.open(path).convert(mode='L')
image = np.asarray(image)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))
ax1.set_title("Початкове зображення")
ax1.imshow(image, cmap='gray')

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