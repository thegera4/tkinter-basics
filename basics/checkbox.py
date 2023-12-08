from tkinter import *

root = Tk()
root.title("Hello checkbox")
root.geometry("500x500")

var = StringVar()
var.set("yes")


def show():
    l = Label(root, text=var.get())
    l.pack()


c = Checkbutton(root, text="Im a checkbox", variable=var, onvalue="yes", offvalue="nope")
c.pack()

btn = Button(root, text="Click", command=show)
btn.pack()

root.mainloop()
