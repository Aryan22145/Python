import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading


class TaskScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Scheduler")

        self.root.geometry("1280x720")

        self.tasks = []

        self.root.configure(bg='#E0E0E0')

        font_gill_sans = ('Gill Sans MT', 13)

        self.task_label = tk.Label(root, text="Task:", bg='#E0E0E0', font=font_gill_sans)
        self.task_entry = tk.Entry(root, width=30, font=font_gill_sans)

        self.time_label = tk.Label(root, text="Time (HH:MM):", bg='#E0E0E0', font=font_gill_sans)
        self.time_entry = tk.Entry(root, width=10, font=font_gill_sans)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg='#4CAF50', fg='white',
                                    font=font_gill_sans)

        self.task_listbox = tk.Listbox(root, width=40, height=10, bg='#FFFFFF', selectbackground='#4CAF50',
                                       selectforeground='white', font=font_gill_sans)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg='#FF5733', fg='white',
                                       font=font_gill_sans)

        self.start_scheduler_button = tk.Button(root, text="Start Scheduler", command=self.start_scheduler,
                                                bg='#008CBA', fg='white', font=font_gill_sans)

        self.task_label.pack(anchor="center", padx=10, pady=10)
        self.task_entry.pack(anchor="center", padx=10, pady=10)
        self.time_label.pack(anchor="center", padx=10, pady=10)
        self.time_entry.pack(anchor="center", padx=10, pady=10)
        self.add_button.pack(anchor="center", padx=10, pady=10)
        self.task_listbox.pack(anchor="center", padx=10, pady=10)
        self.remove_button.pack(anchor="center", padx=10, pady=10)
        self.start_scheduler_button.pack(anchor="center", padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        time_str = self.time_entry.get().strip()

        if not task or not time_str:
            messagebox.showwarning("Error", "Task and time cannot be empty.")
            return

        try:
            task_time = datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            messagebox.showwarning("Error", "Invalid time format. Use HH:MM.")
            return

        self.tasks.append((task, task_time))
        self.update_task_listbox()

        self.task_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Task added successfully!")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()

        if not selected_task_index:
            messagebox.showwarning("Error", "Select a task to remove.")
            return

        task_index = selected_task_index[0]
        del self.tasks[task_index]
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task, task_time in self.tasks:
            self.task_listbox.insert(tk.END, f"{task} - {task_time.strftime('%H:%M')}")

    def execute_tasks(self):
        while True:
            current_time = datetime.now().time()
            for task, task_time in self.tasks:
                if current_time.hour == task_time.hour and current_time.minute == task_time.minute:
                    messagebox.showinfo("Task Alert", f"It's time to: {task}")

            threading.Event().wait(60)

    def start_scheduler(self):
        scheduler_thread = threading.Thread(target=self.execute_tasks, daemon=True)
        scheduler_thread.start()
        self.start_scheduler_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskScheduler(root)
    root.mainloop()
