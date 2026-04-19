import threading
import tkinter as tk
from tkinter import messagebox

from src.input_formatter import format_time_input
from src.scheduler import cancel_shutdown, schedule_shutdown
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

    def on_time_entry_change(_event=None):
        current_value = time_entry.get()
        formatted_value = format_time_input(current_value)

        if current_value != formatted_value:
            time_entry.delete(0, tk.END)
            time_entry.insert(0, formatted_value)

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
                    f"Shutdown scheduled.\nRemaining time: {seconds} seconds.",
                ),
            )

        threading.Thread(target=run_schedule, daemon=True).start()

    def handle_cancel():
        def run_cancel():
            cancel_shutdown()
            window.after(
                0,
                lambda: messagebox.showinfo(
                    "Canceled",
                    "Scheduled shutdown canceled.",
                ),
            )

        threading.Thread(target=run_cancel, daemon=True).start()

    time_entry.bind("<KeyRelease>", on_time_entry_change)

    schedule_button = tk.Button(
        window,
        text="Schedule",
        width=18,
        command=handle_schedule,
    )
    schedule_button.pack(pady=(15, 5))

    cancel_button = tk.Button(
        window,
        text="Cancel",
        width=18,
        command=handle_cancel,
    )
    cancel_button.pack()

    window.mainloop()