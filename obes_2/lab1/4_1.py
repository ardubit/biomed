import numpy as np
import cv2
from matplotlib import pyplot as plt
from imhist import imhist

img = cv2.imread('image0261+gray.png');
# color_map = plt.cm.get_cmap('Greys'); 
color_map = plt.colormaps.get_cmap('Greys');
reversed_color_map = color_map.reversed();

im = plt.imshow(img, cmap=reversed_color_map);
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);
print(hsv);
v = hsv[:, :, 2].copy();
print(v);
v_hist = imhist(v);
print(v_hist);

plt.figure();
plt.bar(np.arange(256), v_hist, align='center');
plt.colorbar(im);
plt.ylabel('Кількість значень (пікселів)');
plt.xlabel('Яскравість');
plt.grid();
plt.show();
