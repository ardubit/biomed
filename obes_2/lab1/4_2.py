import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image0261+gray.png', cv2.IMREAD_GRAYSCALE);
equ = cv2.equalizeHist(img);
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8));
clahe_img = clahe.apply(img);

# img_arr = plt.imread('image0261+gray.png');
# image = plt.imshow(img_arr, cmap='Greys');

color_map = plt.cm.get_cmap('Greys'); 
reversed_color_map = color_map.reversed();

title = ['Початкове зображення', 
         'Гістограма початкового зображення', 
         'Еквалізоване зображення', 'Гістограма', 
         'Контрастне зображення (CLAHE)', 'Гістограма (CLAHE)'];
a = 0;
for i in ([img, equ, clahe_img]):
    plt.figure();
    plt.subplot(121);
    im = plt.imshow(i, cmap='gray');
    plt.title(title[a]);
    a = a+1;
    plt.subplot(122);
    plt.hist(img.ravel(),256,[0,256]);
    # plt.hist(i.ravel(), 256);
    plt.colorbar(im);
    plt.title(title[a]);
    a = a+1;
    plt.show()

