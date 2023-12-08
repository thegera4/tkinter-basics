from tkinter import *
import sqlite3

root = Tk()
root.title("TODO list")
root.geometry("400x400")

db_conn = sqlite3.connect("todo.db")
c = db_conn.cursor()

c.execute("""
    CREATE TABLE if not exists todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    );
""")

db_conn.commit()


# Currying = retrasar la ejecucion de una funcion
def complete_todo(todo_id):
    def _complete_todo():
        todo = c.execute("SELECT * FROM todo WHERE id = ?", (todo_id, )).fetchone()
        c.execute("UPDATE todo SET completed = ? WHERE id = ?", (not todo[3], todo_id))
        db_conn.commit()
        render_todos()

    return _complete_todo


# Currying = retrasar la ejecucion de una funcion
def delete_todo(todo_id):
    def _delete_todo():
        c.execute("DELETE FROM todo WHERE id = ?", (todo_id, ))
        db_conn.commit()
        render_todos()

    return _delete_todo


def render_todos():
    rows = c.execute("SELECT * FROM todo").fetchall()

    # to remove items for screen
    for widget in frame.winfo_children():
        widget.destroy()

    for i in range(0, len(rows)):
        todo_id = rows[i][0]
        completed = rows[i][3]
        description = rows[i][2]
        color = "#d1d1d9" if completed else "#000"
        check = Checkbutton(frame, text=description, fg=color, width=42, anchor="w", command=complete_todo(todo_id))
        check.grid(row=i, column=0, sticky="w")
        delete_btn = Button(frame, text="Delete", command=delete_todo(todo_id))
        delete_btn.grid(row=i, column=1)
        check.select() if completed else check.deselect()


def add_todo():
    todo = e.get()
    if todo:
        c.execute("""
            INSERT INTO todo (description, completed) VALUES (?, ?)
        """, (todo, False))
        db_conn.commit()
        e.delete(0, END)
        render_todos()
    else:
        pass


l = Label(root, text="Todo")
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text="Add", command=add_todo)
btn.grid(row=0, column=2)

frame = LabelFrame(root, text="My todos", padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky="nswe", padx=5)

e.focus()

root.bind("<Return>", lambda x: add_todo())

render_todos()

root.mainloop()
