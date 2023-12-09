from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Logbook - CRM")

conn = sqlite3.connect("crm.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists customer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        company TEXT NOT NULL
    );
""")


def render_customers():
    rows = c.execute("SELECT * FROM customer").fetchall()
    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert("", END, row[0], values=(row[1], row[2], row[3]))


def insert_new_customer(customer):
    c.execute("""
        INSERT INTO customer (name, phone, company) VALUES (?, ?, ?)
    """, (customer["name"], customer["phone"], customer["company"]))
    conn.commit()
    render_customers()


def add_new_customer():
    def save():
        if not name.get():
            messagebox.showerror("Field Required", "The name is required")
            return

        if not phone.get():
            messagebox.showerror("Field Required", "The phone is required")
            return

        if not company.get():
            messagebox.showerror("Field Required", "The company is required")
            return

        customer_dict = {
            "name": name.get(),
            "phone": phone.get(),
            "company": company.get()
        }
        insert_new_customer(customer_dict)
        top.destroy()

    top = Toplevel()
    top.title("New client")
    top.geometry("350x100")

    label_name = Label(top, text="Name")
    name = Entry(top, width=40)
    label_name.grid(row=0, column=0)
    name.grid(row=0, column=1)

    label_phone = Label(top, text="Phone")
    phone = Entry(top, width=40)
    label_phone.grid(row=1, column=0)
    phone.grid(row=1, column=1)

    label_company = Label(top, text="Company")
    company = Entry(top, width=40)
    label_company.grid(row=2, column=0)
    company.grid(row=2, column=1)

    save_btn = Button(top, text="Save", command=save)
    save_btn.grid(row=3, column=1)

    top.mainloop()


def delete_customer():
    item_id = tree.selection()[0]

    customer = c.execute("SELECT * FROM customer WHERE id = ?", (item_id, )).fetchone()
    response = messagebox.askokcancel("Are you sure?", f"Do you want to delete the customer {customer[1]}?")
    if response:
        c.execute("DELETE FROM customer WHERE id =?", (item_id, ))
        conn.commit()
        render_customers()
    else:
        pass


add_btn = Button(root, text="New Customer", command=add_new_customer)
add_btn.grid(column=0, row=0)
del_btn = Button(root, text="Delete Customer", command=delete_customer)
del_btn.grid(column=1, row=0)

tree = ttk.Treeview(root)
tree["columns"] = ("Name", "Phone", "Company")
tree.column("#0", width=0, stretch=NO)
tree.column("Name")
tree.column("Phone")
tree.column("Company")

tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Company", text="Company")
tree.grid(column=0, row=1, columnspan=2)

render_customers()

root.mainloop()
