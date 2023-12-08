from tkinter import *

root = Tk()
root.title("Hello sliders")

vertical = Scale(root, from_=0, to=200, command=lambda x: send())
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()


def send():
    hor = horizontal.get()
    ver = vertical.get()
    print(str(hor) + " " + str(ver))


btn = Button(root, text="Send", command=send)
btn.pack()

root.mainloop()
