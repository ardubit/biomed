import matplotlib.pyplot as plt
import PIL, scipy
from skimage.color import rgb2gray
import skimage

# gray_img_1 = PIL.Image.open("image0261.jpg").convert('LA');
# gray_img_1.save('image0261+gray.png');
# plt.title("Сірошкальне зображення:");
# plt.imshow(gray_img_1);
# plt.show();

gray_img_1 = skimage.io.imread('image0261.jpg');
gray_img_1 = rgb2gray(gray_img_1);
skimage.io.imsave('image0261+gray.png', gray_img_1);
plt.title("Сірошкальне зображення:");
plt.imshow(gray_img_1, cmap = 'gray');
plt.show();

gray_img_2 = skimage.io.imread('image0261+gray.png');
noisy_img = skimage.util.random_noise(gray_img_2, mode = 'speckle');
skimage.io.imsave('image0261+gray+speckle.png', noisy_img);
plt.title("Сірошкальне зображення з додаванням спекл-шуму");
plt.imshow(noisy_img, cmap = 'gray');
plt.show();

# 2.2
filt_orig_3 = scipy.signal.medfilt(noisy_img, kernel_size=3); 
diff_image_3 = noisy_img - filt_orig_3;
filt_orig_9 = scipy.signal.medfilt(noisy_img, kernel_size=9); 
diff_image_9 = noisy_img - filt_orig_9;

plt.figure()
plt.subplot(1, 2, 1);
plt.imshow(diff_image_3, cmap = 'gray');
plt.title("Різницеве зображення, 3x3");
plt.subplot(1, 2, 2);
plt.imshow(diff_image_9, cmap = 'gray');
plt.title("Різницеве зображення, 9x9");
plt.show();

plt.figure();
plt.subplot(1, 2, 1);
plt.imshow(filt_orig_3, cmap = 'gray'); 
plt.title("Фільтроване, 3x3");
plt.subplot(1, 2, 2);
plt.imshow(filt_orig_9, cmap = 'gray');
plt.title("Фільтроване, 9x9");
plt.show();