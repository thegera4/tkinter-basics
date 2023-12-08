from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Hello files")

# root.filename = filedialog.askopenfilename(title="Choose a picture", filetypes=(("PNG Files", "*.png"), ("ALL", "*")))

# l1 = Label(root, text=root.filename)
# l1.pack()

# img = Image.open(root.filename)
# imgTk = ImageTk.PhotoImage(img)

# l2 = Label(root, image=imgTk)
# l2.pack()


def open_file():
    global imgTk
    root.filename = filedialog.askopenfilename(title="Choose a picture",
                                               filetypes=(("JPG Files", "*.jpg"), ("ALL", "*")))
    l1 = Label(root, text=root.filename)
    l1.pack()

    img = Image.open(root.filename)
    imgTk = ImageTk.PhotoImage(img)

    l2 = Label(root, image=imgTk)
    l2.pack()


btn = Button(root, text="Open file", command=open_file)
btn.pack()

root.mainloop()
