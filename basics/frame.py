from tkinter import *

root = Tk()
root.title("Hello frame")
root.geometry('500x500')

frame = LabelFrame(root, text="Login", padx=10, pady=10, borderwidth=10)
no_border_frame = Frame(root, padx=10, pady=10, borderwidth=10)

frame.pack(padx=50, pady=50)
no_border_frame.pack()

label = Label(frame, text="Im inside a frame")
btn = Button(frame, text="Quit", command=root.quit)
btn_nb = Button(no_border_frame, text="Quit", command=root.quit)

label.pack()
btn.pack()
btn_nb.pack()

root.mainloop()
