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
- 🖥️ Clean and minimal graphical interface (GUI)
- ⚡ Fast execution with no installation required
- 🧠 Smart handling of past times (automatically schedules for the next day)

---

## 🖼️ Preview

<img width="397" height="261" alt="image" src="https://github.com/user-attachments/assets/6134e066-008d-4eae-aacc-c5b0bbfecdcd" />


---

## 📦 Download

👉 Go to the latest release:  
https://github.com/juanpbarros/TimeOut/releases

1. Download the `.zip` file  
2. Extract it  
3. Run `TimeOut.exe`  

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
