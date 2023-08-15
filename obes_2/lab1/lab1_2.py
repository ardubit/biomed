import matplotlib.pyplot as plt
import PIL
from PIL import ImageEnhance

im = PIL.Image.open("image0261.jpg");
enhancer = ImageEnhance.Brightness(im);

brightness = 0.25, 0.5, 1, 1.5, 5, 10;
for b in brightness:
    factor = b;
    # print(factor);
    plt.figure(); # створює нове вікно
    plt.title("Ультразвукове зображення плоду, brightness = "+str(factor)); # додає підпис
    im_output = enhancer.enhance(factor); # обробка
    Image = plt.imshow(im_output, cmap='Greys'); 
    plt.colorbar(Image);
    plt.show();

print("OK!");