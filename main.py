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
    root.geometry("750x650")
    root.configure(bg="white")

    tk.Label(
        root,
        text="Smart Task Manager",
        font=("Arial", 24, "bold"),
        bg="white"
    ).pack(pady=20)

    # ------------------------
    # Task Row
    # ------------------------

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

    # ------------------------
    # Search Row
    # ------------------------

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

    # ------------------------
    # Functions
    # ------------------------

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

        selected = task_listbox.get(selection[0])
        index = tasks.index(selected)

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

        selected = task_listbox.get(selection[0])

        tasks.remove(selected)

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

    def show_all():
        refresh_list(tasks)

    def show_active():
        active = []

        for task in tasks:
            if not task.startswith("✔ "):
                active.append(task)

        refresh_list(active)

    def show_completed():
        completed = []

        for task in tasks:
            if task.startswith("✔ "):
                completed.append(task)

        refresh_list(completed)

    # ------------------------
    # Buttons
    # ------------------------

    top_buttons = tk.Frame(root, bg="white")
    top_buttons.pack(pady=5)

    tk.Button(
        top_buttons,
        text="Add Task",
        width=14,
        command=add_task
    ).pack(side="left", padx=3)

    tk.Button(
        top_buttons,
        text="Search",
        width=14,
        command=search_tasks
    ).pack(side="left", padx=3)

    tk.Button(
        top_buttons,
        text="Clear Search",
        width=14,
        command=clear_search
    ).pack(side="left", padx=3)

    filter_buttons = tk.Frame(root, bg="white")
    filter_buttons.pack(pady=5)

    tk.Button(
        filter_buttons,
        text="All",
        width=12,
        command=show_all
    ).pack(side="left", padx=3)

    tk.Button(
        filter_buttons,
        text="Active",
        width=12,
        command=show_active
    ).pack(side="left", padx=3)

    tk.Button(
        filter_buttons,
        text="Completed",
        width=12,
        command=show_completed
    ).pack(side="left", padx=3)

    bottom_buttons = tk.Frame(root, bg="white")
    bottom_buttons.pack(pady=10)

    tk.Button(
        bottom_buttons,
        text="Complete Task",
        width=15,
        command=complete_task
    ).pack(side="left", padx=5)

    tk.Button(
        bottom_buttons,
        text="Delete Task",
        width=15,
        command=delete_task
    ).pack(side="left", padx=5)

    task_entry.bind("<Return>", lambda event: add_task())
    search_entry.bind("<Return>", lambda event: search_tasks())

    root.mainloop()


if __name__ == "__main__":
    main()