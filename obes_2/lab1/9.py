# lab 1, task 9
from tkinter import *
import PIL
from PIL import Image as Pil_image, ImageTk as Pil_imageTk 
from PIL import ImageFilter, ImageEnhance

img1 = r'image0261+gray.png';

def init_img():
    img = PIL.Image.open(img1);
    photo = PIL.ImageTk.PhotoImage(img);
    cv = Canvas(width = 180, height = 180);
    cv.pack(side='top', fill='both', expand='yes');
    label.configure(image=photo);
    label.image=img;
    # cv.create_image(25, 600, image=photo, anchor='nw');
    mainloop();

def filter():
    img = PIL.Image.open(img1).convert('L');
    if var.get() == 1: img_smooth_more = img.filter(ImageFilter.BLUR);
    elif var.get() == 2: img_smooth_more = img.filter(ImageFilter.SMOOTH);
    elif var.get() == 3: img_smooth_more = img.filter(ImageFilter.CONTOUR);
    elif var.get() == 4: img_smooth_more = img.filter(ImageFilter.DETAIL);
    elif var.get() == 5: img_smooth_more = img.filter(ImageFilter.EMBOSS);
    elif var.get() == 6: img_smooth_more = img.filter(ImageFilter.SHARPEN);
    elif var.get() == 7: img_smooth_more = img.filter(ImageFilter.EDGE_ENHANCE);
    elif var.get() == 8: img_smooth_more = img.filter(ImageFilter.EDGE_ENHANCE_MORE);
    
    photo = PIL.ImageTk.PhotoImage(img_smooth_more);
    cv = Canvas(width = 200, height = 200);
    cv.pack(side='top', fill='both', expand='yes');
    # cv.create_image(25, 600, image=photo, anchor='nw');
    label.configure(image=photo);
    label.image=photo;
    mainloop();

window = Tk();
window.title("GUI Image Processing App. L1.9");
window.geometry("400x580");
label = Label(window, font = ('arial', 12, 'bold'));
label.pack();

var = IntVar();
var.set(1);
RBttn1 = Radiobutton(text = "Blur", variable = var,value = 1, font =('arial', 14), command=filter).pack(anchor = W);
RBttn2 = Radiobutton(text = "Smooth", variable = var,value = 2, font =('arial', 14), command=filter).pack(anchor = W);
RBttn3 = Radiobutton(text = "Contour", variable = var,value = 3, font =('arial', 14), command=filter).pack(anchor = W);
RBttn4 = Radiobutton(text = "Details", variable = var,value = 4, font =('arial', 14), command=filter).pack(anchor = W);
RBttn5 = Radiobutton(text = "Emboss", variable = var,value = 5, font =('arial', 14), command=filter).pack(anchor = W);
RBttn6 = Radiobutton(text = "Sharpen", variable = var,value = 6, font =('arial', 14), command=filter).pack(anchor = W);
RBttn7 = Radiobutton(text = "Edge enhance", variable = var,value = 7, font =('arial', 14), command=filter).pack(anchor = W);
RBttn8 = Radiobutton(text = "Edge enhance more", variable = var,value = 8, font =('arial', 14), command=filter).pack(anchor = W);

b = Button(window, text="Початкове зображення", command=init_img);
b.pack();
init_img();           
window.mainloop();
