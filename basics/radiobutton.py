from tkinter import *

root = Tk()
root.title("Radio buttons")

r = IntVar()
r.set(2)

# Radiobutton(root, text="Option 1", variable=r, value=1).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2).pack()
# Radiobutton(root, text="Option 3", variable=r, value=3).pack()

# label = Label(root, textvariable=r)
# label.pack()

fruits = [
    ("apple", "apple"),
    ("pear", "pear"),
    ("orange", "orange"),
    ("grapes", "grapes")
]

initial = StringVar()
initial.set("grapes")

for text, fruit in fruits:
    Radiobutton(root, text=text, variable=initial, value=fruit).pack()

label = Label(root, textvariable=initial)
label.pack()

root.mainloop()
