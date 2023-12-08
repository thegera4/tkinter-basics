from tkinter import *

root = Tk()
root.title("Hello dropdown")
root.geometry("500x500")

lista = ["orange", "apple", "mango", "grapes"]
value = StringVar()
value.set(lista[0])

menu = OptionMenu(root, value, *lista)
menu.pack()


def send():
    l = Label(root, text=value.get())
    l.pack()


btn = Button(root, text="Send", command=send)
btn.pack()

root.mainloop()
