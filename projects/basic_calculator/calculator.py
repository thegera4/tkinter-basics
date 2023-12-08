# Typical calculator app
from tkinter import *

root = Tk()
root.configure(background="#333333")
root.title("Calculator")
root.geometry("386x168")

operation = StringVar()


def press(num):
    operation.set(operation.get() + str(num))
    print(operation.get())


def equal_press():
    try:
        total = str(eval(operation.get()))
        operation.set(total)
    except ValueError:
        operation.set("ERROR")


def clear():
    operation.set("")


display = Entry(root, textvariable=operation, background="#000", fg="#fff")
display.grid(row=0, columnspan=4, sticky="nswe")

btn7 = Button(root, text=" 7 ", fg="#fff", background="#666", command=lambda: press(7))
btn7.grid(row=1, column=0, sticky="nswe")
btn8 = Button(root, text=" 8 ", fg="#fff", background="#666", command=lambda: press(8))
btn8.grid(row=1, column=1, sticky="nswe")
btn9 = Button(root, text=" 9 ", fg="#fff", background="#666", command=lambda: press(9))
btn9.grid(row=1, column=2, sticky="nswe")

btn4 = Button(root, text=" 4 ", fg="#fff", background="#666", command=lambda: press(4))
btn4.grid(row=2, column=0, sticky="nswe")
btn5 = Button(root, text=" 5 ", fg="#fff", background="#666", command=lambda: press(5))
btn5.grid(row=2, column=1, sticky="nswe")
btn6 = Button(root, text=" 6 ", fg="#fff", background="#666", command=lambda: press(6))
btn6.grid(row=2, column=2, sticky="nswe")

btn1 = Button(root, text=" 1 ", fg="#fff", background="#666", command=lambda: press(1))
btn1.grid(row=3, column=0, sticky="nswe")
btn2 = Button(root, text=" 2 ", fg="#fff", background="#666", command=lambda: press(2))
btn2.grid(row=3, column=1, sticky="nswe")
btn3 = Button(root, text=" 3 ", fg="#fff", background="#666", command=lambda: press(3))
btn3.grid(row=3, column=2, sticky="nswe")

btn0 = Button(root, text=" 0 ", fg="#fff", background="#666", command=lambda: press(0))
btn0.grid(row=4, column=0, sticky="nswe", columnspan=2)
btn_dot = Button(root, text=" . ", fg="#fff", background="#666", command=lambda: press("."))
btn_dot.grid(row=4, column=2, sticky="nswe")

btn_add = Button(root, text=" + ", fg="#fff", background="#fe9727", command=lambda: press("+"))
btn_add.grid(row=1, column=3, sticky="nswe")
btn_sub = Button(root, text=" - ", fg="#fff", background="#fe9727", command=lambda: press("-"))
btn_sub.grid(row=2, column=3, sticky="nswe")
btn_mul = Button(root, text=" x ", fg="#fff", background="#fe9727", command=lambda: press("*"))
btn_mul.grid(row=3, column=3, sticky="nswe")
btn_div = Button(root, text=" / ", fg="#fff", background="#fe9727", command=lambda: press("/"))
btn_div.grid(row=4, column=3, sticky="nswe")

btn_equals = Button(root, text=" = ", fg="#fff", background="#fe9727", command=equal_press)
btn_equals.grid(row=5, column=2, sticky="nswe", columnspan=2)
btn_clear = Button(root, text=" CLEAR ", fg="#fff", background="#999", command=clear)
btn_clear.grid(row=5, column=0, sticky="nswe", columnspan=2)

root.mainloop()
