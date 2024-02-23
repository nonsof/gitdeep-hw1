#hello world
# here you can find latter a little project, but if it should be here, let's make a little prgrm here

import tkinter as tk
from tkinter import Tk, filedialog 

def get_credentials():
    def login():
        nonlocal result
        nonlocal file_paths
        username_value = username_entry.get()
        password_value = password_entry.get()
        result = (username_value, password_value, file_paths)
        root.destroy()

    root = Tk()
    root.title("Страница входа")

    root.geometry("800x600")

    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    tk.Label(frame, text="Имя пользователя:").pack(side="top", pady=5)
    username_entry = tk.Entry(frame)
    username_entry.pack(side="top", pady=5)

    tk.Label(frame, text="Пароль:").pack(side="top", pady=5)
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack(side="top", pady=5)

    file_paths = []
    path_labels = []  # Initialize path_labels

    def choose_files():
        nonlocal file_paths
        files = filedialog.askopenfilenames(
            parent=frame,
            title="Выберите файлы"
        )
        if files:
            file_paths.extend(files)
            update_path_labels()

    def update_path_labels():
        for label in path_labels:
            label.destroy()

        for path in file_paths:
            label = tk.Label(frame, text=path)
            label.pack(side="top", pady=5)
            path_labels.append(label)

        files_label.config(text=f"Выбрано файлов: {len(file_paths)}")

    choose_files_button = tk.Button(frame, text="Выбрать файлы", command=choose_files)
    choose_files_button.pack(side="top", pady=10)

    files_label = tk.Label(frame, text="Выбрано файлов: 0")
    files_label.pack(side="top", pady=5)

    tk.Button(frame, text="Войти", command=login).pack(side="top", pady=10)

    result = None

    def on_mouse_scroll(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind("<MouseWheel>", on_mouse_scroll)

    root.mainloop()
    
    return result

# Получение учетных данных
credentials = get_credentials()