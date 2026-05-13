# ⏳ TimeOut

A lightweight desktop application that allows you to schedule your computer to automatically shut down — quickly and effortlessly.

---

## 🚀 Overview

**TimeOut** is a simple yet practical tool designed to help you manage automatic system shutdowns.

Whether you're downloading large files, running tasks overnight, or just want your PC to turn off at a specific time — TimeOut does it for you.

---

## ✨ Features

- 🕒 Schedule shutdown at a specific time (HH:MM)
- ❌ Cancel scheduled shutdown anytime
- ⏱️ Quick time adjustment buttons (+10 min, +1h)
- 🔄 Toggle adjustment mode (Less / More) for quick corrections (-10 min, -1h)
- ❌ Clear input button (×) for fast reset
- 🧠 Smart input formatting (numeric-only with automatic `:`)
- 🖥️ Clean and minimal graphical interface (GUI)
- ⚡ Fast execution with no installation required
- 🔄 Automatic handling of past times (schedules for the next day)

---

## 🖼️ Preview

<img width="423" height="335" alt="image" src="https://github.com/user-attachments/assets/96421b5c-5a52-486f-b2bd-54cd427ba266" />



---

## 📦 Download

👉 Go to the latest release:  
https://github.com/juanpbarros/TimeOut/releases

### How to use

1. Download the `.zip` file  
2. Extract it  
3. Open the folder  
4. Run `TimeOut.exe`  

---

## 🛠️ Technologies

- Python
- Tkinter (GUI)
- PyInstaller (Executable)
- Pytest (Testing)

---

## ▶️ Running Locally

```bash
git clone https://github.com/juanpbarros/TimeOut.git
cd TimeOut

python -m venv .venv
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
python -m src.main
