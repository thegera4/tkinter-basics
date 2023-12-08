from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message box")


def warning():
    messagebox.showwarning("Warning", "Hello msgbox")


def info():
    messagebox.showinfo("Info", "Hello msgbox")


def error():
    messagebox.showerror("Error", "Hello msgbox")


def question():
    response = messagebox.askquestion("Question", "Are you sure?")
    if response == "yes":
        messagebox.showinfo("YES", f"you selected: {response}")
    else:
        messagebox.showerror("NO", f"you selected: {response}")


btn_warning = Button(root, text="Warning", command=warning)
btn_info = Button(root, text="Info", command=info)
btn_error = Button(root, text="Error", command=error)
btn_question = Button(root, text="Question", command=question)

btn_warning.pack()
btn_info.pack()
btn_error.pack()
btn_question.pack()

root.mainloop()
