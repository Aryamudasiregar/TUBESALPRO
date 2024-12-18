import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success
        self.create_login_frame()

    def create_login_frame(self):
        self.frame_login = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_login.place(relwidth=1, relheight=1)

        self.label_username = tk.Label(self.frame_login, text="Username:", bg="#f0f0f0", font=("Arial", 12))
        self.label_username.pack(pady=10)

        self.entry_username = tk.Entry(self.frame_login, font=("Arial", 12))
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(self.frame_login, text="Password:", bg="#f0f0f0", font=("Arial", 12))
        self.label_password.pack(pady=10)

        self.entry_password = tk.Entry(self.frame_login, show="*", font=("Arial", 12))
        self.entry_password.pack(pady=5)

        self.login_button = tk.Button(self.frame_login, text="Login", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "admin":
            self.frame_login.place_forget()
            self.on_login_success()
        else:
            messagebox.showerror("Login Failed", "Username atau password salah")