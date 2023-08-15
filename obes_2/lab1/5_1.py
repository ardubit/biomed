import PIL
from matplotlib import pyplot as plt

img = PIL.Image.open('image0261+gray.png');
width, height = img.size;
left = 100; top = 205; right = 290; bottom = 250; 
im1 = img.crop((left, top, right, bottom));
im1.save('image0261+gray+slice.png', format='JPEG', quality=100);
plt.figure();
plt.imshow(im1, cmap='gray');
plt.figure();
plt.imshow(img, cmap='gray');
plt.plot([left,right,right,left],[top,top,bottom,bottom]);
plt.show();