# Image carousel app
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Carousel")

img1 = ImageTk.PhotoImage(Image.open("../../assets/flask.jpg"))
img2 = ImageTk.PhotoImage(Image.open("../../assets/carousel.jpg"))
img3 = ImageTk.PhotoImage(Image.open("../../assets/ladybug.jpg"))
img4 = ImageTk.PhotoImage(Image.open("../../assets/th.jpg"))

lista = [img1, img2, img3, img4]

label = Label(root, image=img1)
label.grid(row=0, column=0, columnspan=3)


def next_img(img_num):
    global label
    global back_btn
    global next_btn

    label.grid_forget()
    label = Label(root, image=lista[img_num])
    back_btn = Button(root, text=" <- ", command=lambda: prev_img(img_num - 1))
    next_btn = Button(root, text=" -> ", command=lambda: next_img(img_num + 1))

    if img_num == 3:
        next_btn = Button(root, text="N/A", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    back_btn.grid(row=1, column=0)
    next_btn.grid(row=1, column=2)


def prev_img(img_num):
    global label
    global back_btn
    global next_btn

    label.grid_forget()
    label = Label(root, image=lista[img_num])
    back_btn = Button(root, text=" <- ", command=lambda: prev_img(img_num - 1))
    next_btn = Button(root, text=" -> ", command=lambda: next_img(img_num + 1))

    if img_num == 0:
        back_btn = Button(root, text="N/A", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    back_btn.grid(row=1, column=0)
    next_btn.grid(row=1, column=2)


back_btn = Button(root, text="N/A", state=DISABLED)
next_btn = Button(root, text=" -> ", command=lambda: next_img(1))

back_btn.grid(row=1, column=0)
next_btn.grid(row=1, column=2)

root.mainloop()
