import tkinter as tk
import threading
from tkinter import messagebox

from src.scheduler import schedule_shutdown, cancel_shutdown
from src.utils import validate_time


def start_gui():
    window = tk.Tk()
    window.title("TimeOut")
    window.geometry("320x180")
    window.resizable(False, False)

    title_label = tk.Label(window, text="TimeOut", font=("Arial", 16, "bold"))
    title_label.pack(pady=(15, 10))

    time_entry = tk.Entry(window, width=18, font=("Arial", 12), justify="center")
    time_entry.pack(pady=5)
    time_entry.insert(0, "HH:MM")

    def clear_placeholder(_event):
        if time_entry.get() == "HH:MM":
            time_entry.delete(0, tk.END)

    def handle_schedule():
        target_time = time_entry.get().strip()

        if not validate_time(target_time):
            messagebox.showerror("Error", "Enter a valid time in HH:MM format.")
            return

        def run_schedule():
            seconds = schedule_shutdown(target_time)
            window.after(
                0,
                lambda: messagebox.showinfo(
                    "Success",
                    f"Shutdown scheduled.\nRemaining time: {seconds} seconds."
                )
            )

        threading.Thread(target=run_schedule, daemon=True).start()

    def handle_cancel():
        def run_cancel():
            cancel_shutdown()
            window.after(
                0,
                lambda: messagebox.showinfo(
                    "Canceled",
                    "Scheduled shutdown canceled."
                )
            )

        threading.Thread(target=run_cancel, daemon=True).start()

    time_entry.bind("<FocusIn>", clear_placeholder)

    schedule_button = tk.Button(
        window,
        text="Schedule",
        width=18,
        command=handle_schedule
    )
    schedule_button.pack(pady=(15, 5))

    cancel_button = tk.Button(
        window,
        text="Cancel",
        width=18,
        command=handle_cancel
    )
    cancel_button.pack()

    window.mainloop()