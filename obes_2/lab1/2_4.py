import PIL
import matplotlib.pyplot as plt
from PIL import ImageFilter

# 2.4
for i in (ImageFilter.BLUR, ImageFilter.CONTOUR, 
          ImageFilter.DETAIL, ImageFilter.EDGE_ENHANCE, 
          ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.EMBOSS,
          ImageFilter.SMOOTH, ImageFilter.SMOOTH_MORE, 
          ImageFilter.SHARPEN):     
    img = PIL.Image.open('image0261+gray+speckle.png').convert('L');
    img_smooth_more = img.filter(i);
    plt.figure();
    plt.title('Просторова фільтрація. Маска: \n'+str(i));
    plt.imshow(img_smooth_more, cmap = 'gray');
    plt.show();
   