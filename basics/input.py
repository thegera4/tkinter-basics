from tkinter import *

root = Tk()
root.title("Hello input")
root.geometry('500x500')

e = Entry(root, width=60)
e.pack()
e.insert(0, "Enter Text:")


def click():
    txt = e.get()
    text_variable.set(txt)
    value = text_variable.get()
    print(value)
    # l.configure(text=txt)
    e.delete(0, END)


btn = Button(root, text="click", command=click)
btn.pack()

text_variable = StringVar()

l = Label(root, textvariable=text_variable)
l.pack()

root.mainloop()
