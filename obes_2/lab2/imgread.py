import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import rescale
from PIL import Image

# 2.0
path = r'cat.jpeg'
# path = r'cat.png'

# via Mathplot
# image = plt.imread(path)
# image = rescale(image, scale=0.4, mode='reflect', channel_axis=None)

# via PIL
image = Image.open(path).convert(mode='L')
image = np.asarray(image)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))

ax1.set_title("Початкове зображення")
ax1.imshow(image, cmap='gray')
plt.show()