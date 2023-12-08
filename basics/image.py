from tkinter import *

# install Pillow: pip install Pillow
from PIL import ImageTk, Image

root = Tk()
root.title("Images")

# img = Image.open("flask.jpg")
# img.show()

img = ImageTk.PhotoImage(Image.open("../assets/flask.jpg"))
label = Label(image=img)
label.pack()

root.mainloop()
