from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Windows")

# alt 1
# def open_new_window():
# img = ImageTk.PhotoImage(Image.open("../assets/flask.jpg"))
# top = Toplevel()
# top.title("New window")
# label = Label(top, text="Im a text in a second window")
# label2 = Label(top, image=img)
# label.pack()
# label2.pack()
# top.mainloop()


# alt 2
# def open_new_window():
# global img
# img = ImageTk.PhotoImage(Image.open("../assets/flask.jpg"))
# top = Toplevel()
# top.title("New window")
# label = Label(top, text="Im a text in a second window")
# label2 = Label(top, image=img)
# label.pack()
# label2.pack()


# alt 3
def open_new_window(img):
    top = Toplevel()
    top.title("New window")
    label = Label(top, text="Im a text in a second window")
    label2 = Label(top, image=img)
    label.pack()
    label2.pack()
    top.mainloop()


img = ImageTk.PhotoImage(Image.open("../assets/flask.jpg"))
Button(root, text="Click", command=lambda: open_new_window(img)).pack()

root.mainloop()
