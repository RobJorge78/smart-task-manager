import tkinter as tk
from tkinter import messagebox

tasks = []


def main():
    root = tk.Tk()

    root.title("Smart Task Manager")
    root.geometry("700x650")
    root.configure(bg="white")

    title = tk.Label(
        root,
        text="Smart Task Manager",
        font=("Arial", 24, "bold"),
        bg="white"
    )
    title.pack(pady=20)

    task_label = tk.Label(
        root,
        text="Task:",
        font=("Arial", 14),
        bg="white"
    )
    task_label.pack()

    task_entry = tk.Entry(
        root,
        width=40,
        font=("Arial", 14)
    )
    task_entry.pack(pady=10)

    add_button = tk.Button(
        root,
        text="Add Task",
        width=20
    )
    add_button.pack(pady=10)

    separator = tk.Frame(
        root,
        height=2,
        width=500,
        bg="gray"
    )
    separator.pack(pady=15)

    tasks_label = tk.Label(
        root,
        text="Tasks",
        font=("Arial", 16, "bold"),
        bg="white"
    )
    tasks_label.pack()

    task_listbox = tk.Listbox(
        root,
        width=50,
        height=10,
        font=("Arial", 13)
    )
    task_listbox.pack(pady=15)

    def add_task():
        task = task_entry.get().strip()

        if task == "":
            return

        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

    def complete_task():
        selection = task_listbox.curselection()

        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select a task."
            )
            return

        index = selection[0]

        if not tasks[index].startswith("✔ "):
            tasks[index] = "✔ " + tasks[index]

            task_listbox.delete(index)
            task_listbox.insert(index, tasks[index])

    def delete_task():
        selection = task_listbox.curselection()

        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select a task."
            )
            return

        index = selection[0]

        del tasks[index]
        task_listbox.delete(index)

    add_button.config(command=add_task)

    task_entry.bind("<Return>", lambda event: add_task())

    complete_button = tk.Button(
        root,
        text="Complete Task",
        width=20,
        command=complete_task
    )
    complete_button.pack(pady=5)

    delete_button = tk.Button(
        root,
        text="Delete Task",
        width=20,
        command=delete_task
    )
    delete_button.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()