import json

DB_FILE = "question_db.json"

def load_questions():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_questions(questions):
    try:
        with open(DB_FILE, "w") as f:
            json.dump(questions, f, indent=4)
    except IOError as e:
        print(f"Gagal menyimpan soal: {e}")