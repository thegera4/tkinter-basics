from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Hello buttons")

label = Label(root, text="This button was clicked")


def click():
    label.pack()


btn = Button(root, text="Press here", command=click, fg="white", bg="blue")
btn.pack()

root.mainloop()
