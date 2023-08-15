import cv2, skimage
from matplotlib import pyplot as plt
import numpy as np

img1 = r'12 NSCs Neurogel (I) x20 b-tubulin+GFAP.tifscale.tif';
img2 = r'NSCs GFAP+olig-2 (II - 53) x20.tifscale.tif';

for i in ([img1, img2]):
    img = cv2.imread(i, cv2.IMREAD_GRAYSCALE);
    #plt.imshow(img);
    result = skimage.filters.try_all_threshold(img , figsize=(8, 5), verbose=True);
    threshold = skimage.filters.threshold_otsu(img);
    predicted = np.uint8(img > threshold) * 255;
    plt.figure();
    plt.imshow(predicted, cmap='gray');
    canny = cv2.Canny(predicted, threshold1=100, threshold2=200); plt.figure();
    plt.imshow(canny, cmap = "gray");
    plt.show();
