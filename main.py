import tkinter as tk


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

    empty_label = tk.Label(
        root,
        text="(No tasks yet.)",
        font=("Arial", 14),
        bg="white",
        fg="gray"
    )
    empty_label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()