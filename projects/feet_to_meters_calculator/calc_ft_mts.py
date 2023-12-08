# Calculate feet to meters
from tkinter import *

root = Tk()
root.title("Feet to meters")

frame = Frame(root, pady=3, padx=12)
frame.grid(column=0, row=0)

ft = StringVar()
ft_input = Entry(frame, width=7, textvariable=ft)
ft_input.grid(column=1, row=0)

mts = StringVar()
Label(frame, textvariable=mts).grid(column=1, row=1)


def calculate(*args):
    try:
        value = float(ft.get())
        m = int(0.3048 * value * 10000 + 0.5) / 10000
        mts.set(str(m))
    except ValueError:
        mts.set("ERROR")


Button(frame, text="Calculate", command=calculate).grid(column=2, row=2)

Label(frame, text="Feet").grid(column=0, row=0)
Label(frame, text="equals").grid(column=0, row=1)
Label(frame, text="meters").grid(column=2, row=1)

ft_input.focus()

root.bind("<Return>", calculate)
root.mainloop()
