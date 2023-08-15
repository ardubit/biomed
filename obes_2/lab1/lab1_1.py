import numpy as np
import matplotlib.pyplot as plt
import imghdr
import PIL
from PIL import ImageEnhance

path = r'image0261.jpg';
img_arr = plt.imread(path);
ImType = imghdr.what(path);
Size_arr = np.shape(img_arr);
print('Тип зображення: ', ImType);
print('Розміри: '+str(Size_arr[0])+' x '+str(Size_arr[1])+' x '+str(Size_arr[2]));

plt.figure();
Image = plt.imshow(img_arr, cmap='Greys');
plt.title("Ультразвукове зображення плоду (за замовчуванням)"); 
plt.colorbar(Image)
plt.show()

alpha_v = 0.2, 0.4, 1;
for a in alpha_v:
    alpha = a;
    plt.figure();
    plt.title("Ультразвукове зображення плоду, alpha = "+str(alpha));
    Image = plt.imshow(img_arr, cmap='Greys', alpha = alpha);
    plt.colorbar(Image);
    plt.show();

