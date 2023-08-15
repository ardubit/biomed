import matplotlib.pyplot as plt

f_size =4, 5, 6, 9, 16, 19, 47;
quality = 0, 5, 10, 20, 50, 75, 100;
graph = plt.plot(quality, f_size);
plt.title("Залежність ступеня стиснення зображення від параметра якості");
plt.xlabel('Розмір файлу - KB');
plt.ylabel('Cтупінь стиснення файлу');
plt.grid(True);
plt.show();