import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json

# Simpan database soal dalam file JSON
DB_FILE = "question_db.json"

# Fungsi untuk membaca soal dari file JSON
def load_questions():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Fungsi untuk menyimpan soal ke file JSON
def save_questions(questions):
    try:
        with open(DB_FILE, "w") as f:
            json.dump(questions, f, indent=4)
    except IOError as e:
        messagebox.showerror("Error", f"Gagal menyimpan soal: {e}")

# Kelas aplikasi GUI
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kuis")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f0f0")  # Background color
        
        # Menambahkan frame untuk login
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
            self.show_quiz_dashboard()
        else:
            messagebox.showerror("Login Failed", "Username atau password salah")
    
    def show_quiz_dashboard(self):
        self.frame_dashboard = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_dashboard.place(relwidth=1, relheight=1)
        
        self.label_title = tk.Label(self.frame_dashboard, text="Dashboard Kuis", font=("Arial", 16), bg="#f0f0f0")
        self.label_title.pack(pady=20)
        
        self.add_question_button = tk.Button(self.frame_dashboard, text="Tambah Soal", font=("Arial", 12), bg="#FF9800", fg="white", command=self.add_question)
        self.add_question_button.pack(pady=10)
        
        self.start_quiz_button = tk.Button(self.frame_dashboard, text="Mulai Kuis", font=("Arial", 12), bg="#2196F3", fg="white", command=self.start_quiz)
        self.start_quiz_button.pack(pady=10)
        
        self.view_questions_button = tk.Button(self.frame_dashboard, text="Lihat Soal", font=("Arial", 12), bg="#9C27B0", fg="white", command=self.view_questions)
        self.view_questions_button.pack(pady=10)
    
    def add_question(self):
        self.frame_add_question = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_add_question.place(relwidth=1, relheight=1)
        
        self.label_question = tk.Label(self.frame_add_question, text="Masukkan Soal Baru:", font=("Arial", 12), bg="#f0f0f0")
        self.label_question.pack(pady=10)
        
        self.entry_question = tk.Entry(self.frame_add_question, font=("Arial", 12))
        self.entry_question.pack(pady=5)
        
        self.label_answer = tk.Label(self.frame_add_question, text="Masukkan Jawaban:", font=("Arial", 12), bg="#f0f0f0")
        self.label_answer.pack(pady=10)
        
        self.entry_answer = tk.Entry(self.frame_add_question, font=("Arial", 12))
        self.entry_answer.pack(pady=5)
        
        self.save_button = tk.Button(self.frame_add_question, text="Simpan Soal", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.save_question)
        self.save_button.pack(pady=20)
        
        self.cancel_button = tk.Button(self.frame_add_question, text="Batal", font=("Arial", 12), bg="#f44336", fg="white", command=self.cancel_add_question)
        self.cancel_button.pack(pady=10)
    
    def save_question(self):
        question = self.entry_question.get()
        answer = self.entry_answer.get()
        
        if question and answer:
            questions = load_questions()
            questions.append({"question": question, "answer": answer})
            save_questions(questions)
            messagebox.showinfo("Sukses", "Soal berhasil disimpan")
            self.frame_add_question.place_forget()
            self.show_quiz_dashboard()
        else:
            messagebox.showerror("Gagal", "Harap masukkan soal dan jawaban")
    
    def cancel_add_question(self):
        self.frame_add_question.place_forget()
        self.show_quiz_dashboard()

    def start_quiz(self):
        questions = load_questions()
        if not questions:
            messagebox.showerror("Tidak Ada Soal", "Tidak ada soal untuk kuis.")
            return
        
        self.frame_quiz = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_quiz.place(relwidth=1, relheight=1)
        
        self.label_quiz = tk.Label(self.frame_quiz, text="Kuis Dimulai!", font=("Arial", 16), bg="#f0f0f0")
        self.label_quiz.pack(pady=20)
        
        self.current_question_index = 0
        self.score = 0
        self.display_question(questions)

    def display_question(self, questions):
        if self.current_question_index >= len(questions):
            messagebox.showinfo("Kuis Selesai", f"Skor Anda: {self.score}")
            self.frame_quiz.place_forget()
            self.show_quiz_dashboard()
            return
        
        question = questions[self.current_question_index]
        self.label_question = tk.Label(self.frame_quiz, text=question["question"], font=("Arial", 12), bg="#f0f0f0")
        self.label_question.pack(pady=20)
        
        self.entry_answer = tk.Entry(self.frame_quiz, font=("Arial", 12))
        self.entry_answer.pack(pady=5)
        
        self.submit_button = tk.Button(self.frame_quiz, text="Kirim Jawaban", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: self.check_answer(questions))
        self.submit_button.pack(pady=20)
    
    def check_answer(self, questions):
        user_answer = self.entry_answer.get()
        correct_answer = questions[self.current_question_index]["answer"]
        
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
        
        self.current_question_index += 1
        self.display_question(questions)  # Rekursif untuk menampilkan pertanyaan berikutnya

    def view_questions(self):
        questions = load_questions()
        if not questions:
            messagebox.showinfo("Tidak Ada Soal", "Belum ada soal.")
            return
    
        self.frame_view_questions = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_view_questions.place(relwidth=1, relheight=1)
    
        self.label_title = tk.Label(self.frame_view_questions, text="Soal yang Tersedia", font=("Arial", 16), bg="#f0f0f0")
        self.label_title.pack(pady=20)
    
        for index, question in enumerate(questions):
            question_label = tk.Label(self.frame_view_questions, text=question["question"], font=("Arial", 12), bg="#f0f0f0")
            question_label.pack(pady=5)

            edit_button = tk.Button(self.frame_view_questions, text="Edit", font=("Arial", 10), command=lambda idx=index: self.edit_question(idx))
            edit_button.pack(pady=5)

            delete_button = tk.Button(self.frame_view_questions, text="Hapus", font=("Arial", 10), command=lambda idx=index: self.delete_question(idx))
            delete_button.pack(pady=5)  # Add delete button

        self.back_button = tk.Button(self.frame_view_questions, text="Kembali", font=("Arial", 12), bg="#f44336", fg="white", command=self.cancel_view_questions)
        self.back_button.pack(pady=20)

    def edit_question(self, index):
        questions = load_questions()
        question_to_edit = questions[index]

        self.frame_edit_question = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_edit_question.place(relwidth=1, relheight=1)

        self.label_edit_question = tk.Label(self.frame_edit_question, text="Edit Soal:", font=("Arial", 12), bg="#f0f0f0")
        self.label_edit_question.pack(pady=10)

        self.entry_edit_question = tk.Entry(self.frame_edit_question, font=("Arial", 12))
        self.entry_edit_question.insert(0, question_to_edit["question"])
        self.entry_edit_question.pack(pady=5)

        self.label_edit_answer = tk.Label(self.frame_edit_question, text="Edit Jawaban:", font=("Arial", 12), bg="#f0f0f0")
        self.label_edit_answer.pack(pady=10)

        self.entry_edit_answer = tk.Entry(self.frame_edit_question, font=("Arial", 12))
        self.entry_edit_answer.insert(0, question_to_edit["answer"])
        self.entry_edit_answer.pack(pady=5)

        self.save_edit_button = tk.Button(self.frame_edit_question, text="Simpan Perubahan", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: self.save_edited_question(index))
        self.save_edit_button.pack(pady=20)

        self.cancel_edit_button = tk.Button(self.frame_edit_question, text="Batal", font=("Arial", 12), bg="#f44336", fg="white", command=self.cancel_edit_question)
        self.cancel_edit_button.pack(pady=10)

    def save_edited_question(self, index):
        questions = load_questions()
        new_question = self.entry_edit_question.get()
        new_answer = self.entry_edit_answer.get()

        if new_question and new_answer:
            questions[index] = {"question": new_question, "answer": new_answer}
            save_questions(questions)
            messagebox.showinfo("Sukses", "Soal berhasil diperbarui")
            self.frame_edit_question.place_forget()
            self.view_questions()  # Kembali ke tampilan soal
        else:
            messagebox.showerror("Gagal", "Harap masukkan soal dan jawaban yang valid.")

    def cancel_edit_question(self):
        self.frame_edit_question.place_forget()
        self.view_questions()  # Kembali ke tampilan soal
    
    def cancel_view_questions(self):
        self.frame_view_questions.place_forget()
        self.show_quiz_dashboard()

    def delete_question(self, index):
        questions = load_questions()
        if index < len(questions):
            del questions[index]  # Delete the question at the specified index
            save_questions(questions)  # Save the updated list
            messagebox.showinfo("Sukses", "Soal berhasil dihapus")
            self.view_questions()  # Refresh the view
        else:
            messagebox.showerror("Error", "Soal tidak ditemukan")

# Menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()