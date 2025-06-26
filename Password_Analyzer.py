import math
import secrets
import string
import csv
import tkinter as tk
from tkinter import messagebox, ttk, filedialog

# ----------------------------
# Password Strength Functions
# ----------------------------

def calculate_entropy(password):
    pool = 0
    if any(ch.islower() for ch in password):
        pool += 26
    if any(ch.isupper() for ch in password):
        pool += 26
    if any(ch.isdigit() for ch in password):
        pool += 10
    if any(ch in string.punctuation for ch in password):
        pool += len(string.punctuation)
    return len(password) * math.log2(pool) if pool else 0


def generate_stronger_password(length=16):
    pool = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(pool) for _ in range(length))


def get_missing_characters(password):
    missing = []
    if not any(c.islower() for c in password):
        missing.append("lowercase (a-z)")
    if not any(c.isupper() for c in password):
        missing.append("uppercase (A-Z)")
    if not any(c.isdigit() for c in password):
        missing.append("digits (0-9)")
    if not any(c in string.punctuation for c in password):
        missing.append("special characters (!@#$ etc.)")
    return ", ".join(missing) if missing else "None"

# ----------------------------
# CSV Scan and Report Functions
# ----------------------------

def scan_file(filename='passwords.csv'):
    password_report = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or not row[0].strip():
                continue
            password = row[0].strip()
            entropy = calculate_entropy(password)
            missing = get_missing_characters(password)
            if entropy < 60:
                weakness = "weak"
                strong_pass = generate_stronger_password(20)
            else:
                weakness = "strong"
                strong_pass = ""

            password_report.append((password, entropy, weakness, missing, strong_pass))
    return password_report


def export_report(filename='report.csv', password_report=None):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['password', 'entropy', 'status', 'missing elements', 'strong password'])
        for password, entropy, weakness, missing, strong_pass in password_report:
            writer.writerow([password, f'{entropy:.2f}', weakness, missing, strong_pass])
    messagebox.showinfo("Export Report", f"Exported password report to {filename}")

# ----------------------------
# GUI Functions
# ----------------------------

def analyze_password():
    password = password_input.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    entropy = calculate_entropy(password)
    missing = get_missing_characters(password)

    if entropy < 60:
        strong_pass = generate_stronger_password(20)
        feedback = f"Weak password (Entropy: {entropy:.2f})\nMissing: {missing}\nSuggested strong password: {strong_pass}"
    else:
        feedback = f"Strong password (Entropy: {entropy:.2f})\nMissing (optional improvements): {missing}"

    messagebox.showinfo("Analysis Result", feedback)


def show_report_table(password_report):
    table_window = tk.Toplevel(root)
    table_window.title("Password Report Table")

    tree = ttk.Treeview(
        table_window,
        columns=('Password', 'Entropy', 'Status', 'Missing', 'Strong Password'),
        show='headings'
    )
    tree.heading('Password', text='Password')
    tree.heading('Entropy', text='Entropy')
    tree.heading('Status', text='Status')
    tree.heading('Missing', text='Missing Elements')
    tree.heading('Strong Password', text='Strong Password Suggestion')

    tree.pack(fill='both', expand=True)

    for password, entropy, weakness, missing, strong_pass in password_report:
        tree.insert('', 'end', values=(password, f'{entropy:.2f}', weakness, missing, strong_pass))


def scan_file_report():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not filepath:
        return

    password_report = scan_file(filepath)
    if password_report:
        export_file = filepath.rsplit('.', 1)[0] + '_report.csv'
        export_report(export_file, password_report)
        show_report_table(password_report)
    else:
        messagebox.showinfo("Analysis Result", "No passwords found in the file.")

# ----------------------------
# GUI Layout
# ----------------------------

root = tk.Tk()
root.title("Password Analyzer Tool")

label = ttk.Label(root, text='Enter password to analyze:')
label.pack(pady=10)

password_input = ttk.Entry(root, show='*', width=40)
password_input.pack(pady=5)

analyze_button = ttk.Button(root, text='Analyze Password', command=analyze_password)
analyze_button.pack(pady=10)

scan_button = ttk.Button(root, text='Scan CSV for Passwords and Export Report', command=scan_file_report)
scan_button.pack(pady=10)

root.mainloop()
