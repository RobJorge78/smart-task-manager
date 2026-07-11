import tkinter as tk

tasks = []


def main():
    root = tk.Tk()

    root.title("Smart Task Manager")
    root.geometry("700x500")
    root.configure(bg="white")

    title = tk.Label(
        root,
        text="Smart Task Manager",
        font=("Arial", 24, "bold"),
        bg="white"
    )
    title.pack(pady=25)

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
    add_button.pack(pady=15)

    separator = tk.Frame(
        root,
        height=2,
        width=500,
        bg="gray"
    )
    separator.pack(pady=20)

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
    task_listbox.pack(pady=10)

    def add_task():
        task = task_entry.get().strip()

        if task == "":
            return

        tasks.append(task)

        task_listbox.insert(tk.END, task)

        task_entry.delete(0, tk.END)

    add_button.config(command=add_task)

    # Allow pressing Enter to add a task
    task_entry.bind("<Return>", lambda event: add_task())

    root.mainloop()


if __name__ == "__main__":
    main()