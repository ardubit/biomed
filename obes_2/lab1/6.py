import cv2, skimage
from matplotlib import pyplot as plt
import numpy as np

im1_arr = cv2.imread('image0261+gray+slice1.png', cv2.IMREAD_GRAYSCALE);
result = skimage.filters.try_all_threshold(im1_arr, figsize=(8, 5), verbose=True); 
threshold = skimage.filters.threshold_otsu(im1_arr);
predicted = np.uint8(im1_arr > threshold) * 255;
plt.figure();
plt.imshow(predicted, cmap='gray');
plt.show();

sobel = cv2.Sobel(predicted, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5); 
canny = cv2.Canny(predicted, threshold1=200, threshold2=400);
gauss = cv2.GaussianBlur(predicted,(5,5),0);
plt.figure();
plt.imshow(sobel.astype(np.uint8), cmap = "gray");
plt.title("Sobel");
plt.figure();
plt.imshow(canny, cmap = "gray");
plt.title("Canny");
plt.figure();
plt.imshow(gauss, cmap = "gray");
plt.title("Gauss");
plt.show();