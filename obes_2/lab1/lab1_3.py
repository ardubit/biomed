import matplotlib.pyplot as plt
import PIL

im = PIL.Image.open("image0261.jpg");
print(im.format, im.size, im.mode);
print("Байт: " + str(len(im.fp.read())));

quality = 0, 5, 10, 20, 50, 75, 100;

# debug
print(len(quality));
r = range(len(quality));
print(r);

# Збереження у файл
for i in range(len(quality)):
    im.save("img-"+str(quality[i])+'.jpeg', format='JPEG', subsampling=0, quality=quality[i]);
    print(i);

# Побудувати залежність ступеня стиснення зображення від параметра якості.
# Розмір зображення Байт, якість.

plt.figure();

# for b in brightness:
#     factor = b;
#     # print(factor);
#     plt.figure(); # створює нове вікно
#     plt.title("Ультразвукове зображення плоду, brightness = "+str(factor)); # додає підпис
#     im_output = enhancer.enhance(factor); # обробка
#     Image = plt.imshow(im_output, cmap='Greys'); 
#     plt.colorbar(Image);
#     plt.show();

print("OK!");