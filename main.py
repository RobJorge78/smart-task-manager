import json
import os
import tkinter as tk
from tkinter import messagebox

DATA_FILE = os.path.join("data", "tasks.json")
tasks = []


def load_tasks():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

    except (FileNotFoundError, json.JSONDecodeError):
        pass

    return []


def save_tasks():
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def main():
    global tasks

    tasks = load_tasks()

    root = tk.Tk()
    root.title("Smart Task Manager")
    root.geometry("750x600")
    root.configure(bg="white")

    title = tk.Label(
        root,
        text="Smart Task Manager",
        font=("Arial", 24, "bold"),
        bg="white"
    )
    title.pack(pady=20)

    # -------------------------
    # Task Input Row
    # -------------------------
    task_frame = tk.Frame(root, bg="white")
    task_frame.pack(pady=10)

    tk.Label(
        task_frame,
        text="Task:",
        font=("Arial", 14),
        bg="white"
    ).pack(side="left", padx=5)

    task_entry = tk.Entry(
        task_frame,
        width=35,
        font=("Arial", 14)
    )
    task_entry.pack(side="left", padx=5)

    # -------------------------
    # Search Row
    # -------------------------
    search_frame = tk.Frame(root, bg="white")
    search_frame.pack(pady=10)

    tk.Label(
        search_frame,
        text="Search:",
        font=("Arial", 14),
        bg="white"
    ).pack(side="left", padx=5)

    search_entry = tk.Entry(
        search_frame,
        width=35,
        font=("Arial", 14)
    )
    search_entry.pack(side="left", padx=5)

    # -------------------------
    # Task List
    # -------------------------
    separator = tk.Frame(root, bg="gray", height=2, width=650)
    separator.pack(pady=15)

    tk.Label(
        root,
        text="Tasks",
        font=("Arial", 16, "bold"),
        bg="white"
    ).pack()

    task_listbox = tk.Listbox(
        root,
        width=60,
        height=12,
        font=("Arial", 13)
    )
    task_listbox.pack(pady=15)

    def refresh_list(task_list):
        task_listbox.delete(0, tk.END)

        for task in task_list:
            task_listbox.insert(tk.END, task)

    refresh_list(tasks)

    # -------------------------
    # Functions
    # -------------------------

    def add_task():
        task = task_entry.get().strip()

        if task == "":
            return

        tasks.append(task)

        save_tasks()
        refresh_list(tasks)

        task_entry.delete(0, tk.END)

    def complete_task():
        selection = task_listbox.curselection()

        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select a task."
            )
            return

        displayed_task = task_listbox.get(selection[0])
        index = tasks.index(displayed_task)

        if not tasks[index].startswith("✔ "):
            tasks[index] = "✔ " + tasks[index]

        save_tasks()
        refresh_list(tasks)

    def delete_task():
        selection = task_listbox.curselection()

        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select a task."
            )
            return

        displayed_task = task_listbox.get(selection[0])

        tasks.remove(displayed_task)

        save_tasks()
        refresh_list(tasks)

    def search_tasks():
        keyword = search_entry.get().strip().lower()

        if keyword == "":
            refresh_list(tasks)
            return

        filtered = []

        for task in tasks:
            if keyword in task.lower():
                filtered.append(task)

        refresh_list(filtered)

    def clear_search():
        search_entry.delete(0, tk.END)
        refresh_list(tasks)

    # -------------------------
    # Buttons
    # -------------------------

    button_frame1 = tk.Frame(root, bg="white")
    button_frame1.pack(pady=5)

    add_button = tk.Button(
        button_frame1,
        text="Add Task",
        width=15,
        command=add_task
    )
    add_button.pack(side="left", padx=5)

    search_button = tk.Button(
        button_frame1,
        text="Search",
        width=15,
        command=search_tasks
    )
    search_button.pack(side="left", padx=5)

    clear_button = tk.Button(
        button_frame1,
        text="Clear Search",
        width=15,
        command=clear_search
    )
    clear_button.pack(side="left", padx=5)

    button_frame2 = tk.Frame(root, bg="white")
    button_frame2.pack(pady=10)

    complete_button = tk.Button(
        button_frame2,
        text="Complete Task",
        width=15,
        command=complete_task
    )
    complete_button.pack(side="left", padx=5)

    delete_button = tk.Button(
        button_frame2,
        text="Delete Task",
        width=15,
        command=delete_task
    )
    delete_button.pack(side="left", padx=5)

    task_entry.bind("<Return>", lambda event: add_task())
    search_entry.bind("<Return>", lambda event: search_tasks())

    root.mainloop()


if __name__ == "__main__":
    main()