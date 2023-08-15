import pywt
from skimage import io, transform
from scipy.fftpack import dct
import scipy.fft as fft
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

path = f'validation_augmented_data/'
path_res = f'data/'
SIZE = 450


def normalizing(image_name):
    img = cv2.imread(path + image_name, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # .IMREAD_COLOR .IMREAD_GRAYSCALE .IMREAD_UNCHANGED .COLOR_BGR2GRAY

    img_resized = cv2.resize(img, (SIZE, SIZE))
    img_write = cv2.cvtColor(img_resized, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'data/resized_' + str(SIZE) + '_' + image_name, img_write)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.title('Початкове зображення')
    plt.imshow(img, cmap="gray")

    plt.subplot(1, 2, 2)
    plt.title('Нормалізоване до розміру 450 * 450 пікселів')
    plt.imshow(img_resized, cmap="gray")
    plt.show()


def rgb_visualization(image_name):
    image_array = cv2.imread(path_res + image_name, cv2.IMREAD_COLOR)
    image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)

    # b, g, r = image_array[:, :, 0], image_array[:, :, 1], image_array[:, :, 2]
    b, g, r = cv2.split(image_array)

    zeros = np.zeros(image_array.shape[:2], dtype="uint8")
    # (:, :, 0) represents Blue channel
    # (:, :, 1) represents Green channel
    # (:, :, 2) represents Red channel
    # (:, :, 3) represents Transparency channel

    fig, ax = plt.subplots(nrows=2, ncols=3)
    r_channel = cv2.merge([r, zeros, zeros])
    g_channel = cv2.merge([zeros, g, zeros])
    b_channel = cv2.merge([zeros, zeros, b])

    r_channel_g = Image.fromarray(r)
    g_channel_g = Image.fromarray(g)
    b_channel_g = Image.fromarray(b)

    ax[0][0].imshow(r_channel)
    ax[0][1].imshow(g_channel)
    ax[0][2].imshow(b_channel)

    ax[1][0].imshow(r_channel_g, cmap='gray')
    ax[1][1].imshow(g_channel_g, cmap='gray')
    ax[1][2].imshow(b_channel_g, cmap='gray')

    ax[0][0].set_title("Канал: Red")
    ax[0][1].set_title("Канал: Green")
    ax[0][2].set_title("Канал: Blue")

    ax[0][0].axis('off')
    ax[0][1].axis('off')
    ax[0][2].axis('off')
    ax[1][0].axis('off')
    ax[1][1].axis('off')
    ax[1][2].axis('off')

    fig.tight_layout()
    fig.subplots_adjust(wspace=0, hspace=0, left=0,
                        right=1, bottom=0, top=0.97)
    x = np.linspace(0, image_array.shape[0], image_array.shape[0])
    y = np.linspace(0, image_array.shape[1], image_array.shape[1])
    X, Y = np.meshgrid(x, y)

    fig3d = plt.figure()
    ax1 = fig3d.add_subplot(2, 3, 1, projection='3d')
    ax2 = fig3d.add_subplot(2, 3, 2, projection='3d')
    ax3 = fig3d.add_subplot(2, 3, 3, projection='3d')
    ax4 = fig3d.add_subplot(2, 3, 4, projection='3d')
    ax5 = fig3d.add_subplot(2, 3, 5, projection='3d')
    ax6 = fig3d.add_subplot(2, 3, 6, projection='3d')

    # 3D Подання зображення
    ax1.plot_surface(X, Y, r, cmap='Reds')
    ax2.plot_surface(X, Y, g, cmap='Greens')
    ax3.plot_surface(X, Y, b, cmap='Blues')

    # ax1.plot_surface(X, Y, r_channel[:, :, 0], cmap='Reds')
    # ax2.plot_surface(X, Y, g_channel[:, :, 1], cmap='Greens')
    # ax3.plot_surface(X, Y, b_channel[:, :, 2], cmap='Blues')

    ax4.plot_surface(X, Y, r, cmap='Greys')
    ax5.plot_surface(X, Y, g, cmap='Greys')
    ax6.plot_surface(X, Y, b, cmap='Greys')

    ax1.set_title("Канал: Red")
    ax2.set_title("Канал: Green")
    ax3.set_title("Канал: Blue")

    fig3d.tight_layout()
    fig3d.subplots_adjust(wspace=0, hspace=0, left=0,
                          right=1, bottom=0, top=0.97)
    plt.show()


def mid_iris(image_name):
    image = cv2.imread(path_res + image_name)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    mid_row = image_gray[image_gray.shape[0] // 2, :]
    x = range(len(mid_row))

    plt.plot(x, mid_row)
    plt.xlabel('Позиція пікселя')
    plt.ylabel('Яскравість пікселя')
    plt.title('Зріз матриці на рівні середини зіниці ока ' + image_name)
    plt.grid()
    plt.show()


def hist(image_name):
    # Обчислення гістограми
    image = cv2.imread(path_res + image_name, 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    histogram_normalized = histogram / (image.shape[0] * image.shape[1])
    histogram_normalized *= 255

    cumulative_sum = histogram_normalized.cumsum()

    equalized_image = np.interp(image, range(256), cumulative_sum)
    equalized_image = equalized_image.astype(np.uint8)

    plt.subplot(121)
    plt.plot(histogram)
    plt.title('Розподіл яскравостей зображення ' + image_name)
    plt.xlabel('Рівні сірого')
    plt.ylabel('Частота появи значення')
    plt.grid()

    plt.subplot(122)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Еквалізоване (контрастне) зображення ' + image_name)
    plt.show()

    img_write = cv2.cvtColor(equalized_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'data/eq_' + image_name, img_write)


# 1
normalizing('img_001_001.jpg')
normalizing('img_002_001.jpg')

# 2,3
rgb_visualization('resized_450_img_001_001.jpg')
rgb_visualization('resized_450_img_002_001.jpg')
mid_iris('resized_450_img_001_001.jpg')
mid_iris('resized_450_img_002_001.jpg')

# 4.1
# Обчислення гістограми
hist('resized_450_img_001_001.jpg')
hist('resized_450_img_002_001.jpg')

# 4.2
# Подання в полярній системі координат


def unwrap_iris(image_name, center, inner_radius, outer_radius):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Визначення центру та меж зіниці
    # Тест
    # center = (250, 250)
    # inner_radius = 50
    # outer_radius = 200

    # Перетворення в полярну систему координат
    polar_image = np.zeros((outer_radius-inner_radius, 360), dtype=np.uint8)

    for r in range(inner_radius, outer_radius):
        for theta in range(360):
            x = int(center[0] + r * np.cos(np.deg2rad(theta)))
            y = int(center[1] + r * np.sin(np.deg2rad(theta)))
            polar_image[r-inner_radius, theta] = image[y, x]

    # Візуалізація зображення полярної системи координат
    plt.figure()
    plt.title('Розгорнуте зображення: ' + image_name)
    plt.imshow(polar_image, cmap='gray')
    plt.show()

    img_write = cv2.cvtColor(polar_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'data/polar_' + image_name, img_write)


unwrap_iris('eq_resized_450_img_001_001.jpg', (225, 225), 50, 200)
unwrap_iris('eq_resized_450_img_002_001.jpg', (225, 225), 50, 200)

# Виділення зони інтересу на прямокутному зображенні


def roi(image_name):
    image = cv2.imread(path_res + image_name)

    x = 0
    y = 50
    width = 200
    height = 50

    # Вирізання ROI з зображення
    roi = image[y:y+height, x:x+width]

    # Візуалізація зображення полярної системи координат
    params = [x, y, width, height]
    plt.figure()
    plt.title('Зона інтересу (ROI): x, y, w, h ' +
              str(params) + ' ' + image_name)
    plt.imshow(roi, cmap='gray')
    plt.show()

    img_write = cv2.cvtColor(roi, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'data/roi_' + image_name, img_write)


roi('polar_eq_resized_450_img_001_001.jpg')
roi('polar_eq_resized_450_img_002_001.jpg')

# 5. Дискретне перетворення Фур’є
# from scipy.fftpack import dct2


def FFT(image_name):
    image = cv2.imread(path_res + image_name)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Обчислення дискретного перетворення Фур'є
    dft = np.fft.fft2(image)
    # Перенесення нульової частоти в центр спектра
    shifted_dft = np.fft.fftshift(dft)
    # Обчислення амплітудного спектра
    magnitude_spectrum = 20 * np.log(np.abs(shifted_dft))

    x, y = np.meshgrid(np.linspace(0, abs(fft.fftshift(dft)).shape[0], num=abs(fft.fftshift(dft)).shape[0]),
                       np.linspace(0, abs(fft.fftshift(dft)).shape[1], num=abs(fft.fftshift(dft)).shape[1]))

    plt.figure()
    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122, projection='3d')
    ax1.set_title("2D Дискр. перетворення Фур’є: " + image_name)
    ax2.set_title("3D Дискр. перетворення Фур’є: " + image_name)

    ax1.imshow(np.log10(abs(fft.fftshift(dft))))
    ax2.plot_surface(x, y, np.log10(abs(fft.fftshift(dft.T))), cmap='coolwarm')
    plt.show()

    # DCT
    # Обчислення 2D DCT
    # dct_image = transform.dct(transform.dct(image, type=2, norm='ortho'), type=2, norm='ortho')
    # plt.imshow('DCT Image', np.abs(dct_image))
    # plt.show()

    img_dct = dct(dct(image, norm='ortho'), axis=0, norm='ortho')
    x, y = np.meshgrid(np.linspace(0, img_dct.shape[0], num=img_dct.shape[0]),
                       np.linspace(0, img_dct.shape[1], num=img_dct.shape[1]))

    plt.figure()
    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122, projection='3d')
    ax1.set_title("2D Дискр. косинусне перетворення: " + image_name)
    ax2.set_title("3D Дискр. косинусне перетворення: " + image_name)
    ax1.imshow(np.log10(abs(img_dct)))
    ax2.plot_surface(x.T, y.T, np.log10(abs(img_dct)), cmap='coolwarm')
    plt.show()


FFT('roi_polar_eq_resized_450_img_001_001.jpg')
FFT('roi_polar_eq_resized_450_img_002_001.jpg')

# Вейвлет перетворення


def wavelet(image_name):
    image = cv2.imread(path_res + image_name)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_wav = pywt.wavedec2(image, wavelet='sym5', level=3)
    colormap_wav = 'plasma'

    fig, ax = plt.subplots(ncols=2, nrows=2)
    fig.suptitle(
        'Двовимірне вейвлет-перетворення. Коеф. апроксимації: 3. ' + 'File: ' + image_name)
    ax[0, 0].imshow(img_wav[0], cmap=colormap_wav)
    ax[0, 1].imshow(img_wav[1][0], cmap=colormap_wav)
    ax[1, 0].imshow(img_wav[2][0], cmap=colormap_wav)
    ax[1, 1].imshow(img_wav[3][0], cmap=colormap_wav)

    ax[0, 0].set_title('Coef. Approximation ')
    ax[0, 1].set_title('Coef. Horizontal Detail ')
    ax[1, 0].set_title('Coef. Vertical Detail ')
    ax[1, 1].set_title('Coef. Diagonal Detail ')

    ax[0, 0].axis('off')
    ax[0, 1].axis('off')
    ax[1, 0].axis('off')
    ax[1, 1].axis('off')
    fig.tight_layout()
    fig.subplots_adjust(wspace=0, hspace=0, left=0,
                        right=1, bottom=0, top=0.97)

    fig, ax = plt.subplots(ncols=2, nrows=2)
    fig.suptitle(
        'Двовимірне вейвлет-перетворення. Коеф. апроксимації: 2. ' + 'File: ' + image_name)
    ax[0, 0].imshow(img_wav[0], cmap=colormap_wav)
    ax[0, 1].imshow(img_wav[1][1], cmap=colormap_wav)
    ax[1, 0].imshow(img_wav[2][1], cmap=colormap_wav)
    ax[1, 1].imshow(img_wav[3][1], cmap=colormap_wav)

    ax[0, 0].set_title('Coef. Approximation ')
    ax[0, 1].set_title('Coef. Horizontal Detail ')
    ax[1, 0].set_title('Coef. Vertical Detail ')
    ax[1, 1].set_title('Coef. Diagonal Detail ')

    ax[0, 0].axis('off')
    ax[0, 1].axis('off')
    ax[1, 0].axis('off')
    ax[1, 1].axis('off')
    fig.tight_layout()
    fig.subplots_adjust(wspace=0, hspace=0, left=0,
                        right=1, bottom=0, top=0.97)

    fig, ax = plt.subplots(ncols=2, nrows=2)
    fig.suptitle(
        'Двовимірне вейвлет-перетворення. Коеф. апроксимації: 1. ' + 'File: ' + image_name)
    ax[0, 0].imshow(img_wav[0], cmap=colormap_wav)
    ax[0, 1].imshow(img_wav[1][2], cmap=colormap_wav)
    ax[1, 0].imshow(img_wav[2][2], cmap=colormap_wav)
    ax[1, 1].imshow(img_wav[3][2], cmap=colormap_wav)

    ax[0, 0].set_title('Coef. Approximation ')
    ax[0, 1].set_title('Coef. Horizontal Detail ')
    ax[1, 0].set_title('Coef. Vertical Detail ')
    ax[1, 1].set_title('Coef. Diagonal Detail ')

    ax[0, 0].axis('off')
    ax[0, 1].axis('off')
    ax[1, 0].axis('off')
    ax[1, 1].axis('off')
    fig.tight_layout()
    fig.subplots_adjust(wspace=0, hspace=0, left=0,
                        right=1, bottom=0, top=0.97)
    plt.show()


wavelet('roi_polar_eq_resized_450_img_001_001.jpg')
wavelet('roi_polar_eq_resized_450_img_002_001.jpg')
