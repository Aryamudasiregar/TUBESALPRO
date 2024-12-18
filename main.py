import tkinter as tk
from login import Login
from dashboard import Dashboard

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kuis")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f0f0")
        
        self.login_interface = LoginInterface(root, self.show_dashboard)

    def show_dashboard(self):
        self.dashboard_interface = DashboardInterface(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
