import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do Siyahısı")
        self.root.geometry("400x400")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_btn = tk.Button(root, text="Əlavə et", command=self.add_task)
        self.add_btn.pack(pady=5)

        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)

        self.delete_btn = tk.Button(root, text="Sil", command=self.delete_task)
        self.delete_btn.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Xəta", "Zəhmət olmasa bir tapşırıq yazın.")

    def delete_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            task = self.listbox.get(selected_task)
            self.tasks.remove(task)
            self.update_listbox()
        else:
            messagebox.showwarning("Xəta", "Silmək üçün tapşırıq seçin.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()