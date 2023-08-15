import matplotlib.pyplot as plt
import PIL, skimage, scipy
from skimage.color import rgb2gray

im = PIL.Image.open("NSCs GFAP+olig-2 (II - 53) x20.tifscale.tif");
Image = plt.imshow(im);
plt.title("Початкове зображення:");
plt.show();

grayImg = PIL.Image.open("NSCs GFAP+olig-2 (II - 53) x20.tifscale.tif").convert('LA');
grayImg.save('greyscale.png')
plt.imshow(grayImg);
plt.title("Сірошкальне зображення:");
plt.show();

# 2.1
img_arr = plt.imread('image0261.jpg');
noisyImg = skimage.util.random_noise(img_arr, mode = 'speckle');
# Побудова та вивід спектру
plt.figure()
plt.subplot(1,2,1)
plt.title("Початкове зображення:");
plt.imshow(img_arr);

plt.subplot(1,2,2)
plt.title("Сірошкальне зображення з додаванням спекл-шуму");
plt.imshow(noisyImg);
plt.show();

