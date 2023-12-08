from tkinter import *

root = Tk()
root.title("Hi tkinter")
root.geometry('500x500')

label1 = Label(root, text="My first label with tkinter")
label2 = Label(root, text="My second label with tkinter")
label3 = Label(root, text="                ")

label1.grid(row=0, column=0)
label3.grid(row=1, column=1)
label2.grid(row=10, column=10)

root.mainloop()
