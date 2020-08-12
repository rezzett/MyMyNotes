from tkinter import *
from task import Task

root = Tk()
root.geometry("800x600")

input_field = Entry(root, fg="white", bg="gray", bd=2)
input_field.pack()


frame = Frame(root)
frame.pack()

tasks = []


def tasks_list_view(tasks_list):
    global frame
    for widget in frame.winfo_children():
        widget.destroy()
    for task in tasks_list:
        Label(frame, text=task.content, fg="white").pack()


def add_btn_handler():
    tasks.append(Task(input_field.get()))
    input_field.delete(0, END)
    tasks_list_view(tasks)


addButton = Button(root, bg="green", text="Click on me!", command=add_btn_handler, fg="white")
addButton.pack()

root.mainloop()
