from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello treeview")

tree = ttk.Treeview(root)
tree["columns"] = ("Name", "Phone", "Company")

# tree.column("#0")
tree.column("#0", width=0, stretch=NO) # to delete column
tree.column("Name")
tree.column("Phone")
tree.column("Company")

# tree.heading("#0", text="id")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Company", text="Company")

tree.grid(column=0, row=0)

tree.insert("", END, "row1", values=("One", "Two", "Three"), text="John Smith")
tree.insert("", END, "row2", values=("Four", "Five", "Six"), text="Jane Doe")
tree.insert("", END, "row3", values=("Seven", "Eight", "Nine"), text="Joe")

root.mainloop()
