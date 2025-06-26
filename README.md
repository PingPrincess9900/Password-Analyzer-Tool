# 🔐 Password Analyzer Tool 

A Python-based GUI application that analyzes password strength using entropy. The tool identifies weaknesses in passwords, suggests what character types are missing (e.g., uppercase, digits), generates stronger alternatives, and allows bulk scanning of passwords via CSV files. It also exports a detailed report and displays results in a user-friendly table format.

---

 ##🧠 Features

- ✔️ Entropy-based password strength analysis
- ✔️ Detects and reports missing character types (lowercase, uppercase, digits, symbols)
- ✔️ Generates strong password suggestions for weak entries
- ✔️ Simple and intuitive GUI using Tkinter
- ✔️ Analyze individual passwords or scan a full list from a CSV file
- ✔️ Displays results in a sortable GUI table
- ✔️ Exports results to a structured CSV report

---

## 💻 Technologies Used

- **Python 3**
- **Tkinter** for GUI
- **CSV** for input/output handling
- **Secrets** and **Math** libraries for entropy calculation and password generation

---


## 🔁 Workflow

1. **User Input (Manual Check):**
   - The user enters a password into the GUI input field.
   - The tool calculates entropy based on character variety and length.
   - It checks for missing character types (lowercase, uppercase, digits, symbols).
   - If weak, it suggests a strong password and displays all findings.

2. **Bulk Scan from CSV:**
   - The user uploads a CSV file where each row contains a password.
   - The tool analyzes each password:
     - Calculates entropy
     - Flags as weak or strong
     - Identifies missing character types
     - Suggests a strong replacement for weak passwords
   - Results are shown in a GUI table.

3. **Export Report:**
   - After scanning, a CSV report is automatically generated.
   - Report includes: password, entropy, strength status, missing elements, suggested password.


---

## 🙌 Acknowledgements

- This project was developed as part of an educational assignment to understand password security and GUI-based applications in Python.



