import threading
import tkinter as tk
from tkinter import messagebox

from src.input_formatter import format_time_input
from src.scheduler import cancel_shutdown, schedule_shutdown
from src.time_helper import add_minutes_to_time
from src.utils import validate_time


def start_gui():
    window = tk.Tk()
    window.title("TimeOut")
    window.geometry("320x220")
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

    def handle_time_increment(minutes: int):
        current_value = time_entry.get().strip()

        if current_value and not validate_time(current_value):
            messagebox.showerror("Error", "Enter a valid time before adding minutes.")
            return

        updated_time = add_minutes_to_time(current_value, minutes)

        time_entry.delete(0, tk.END)
        time_entry.insert(0, updated_time)

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

    increment_frame = tk.Frame(window)
    increment_frame.pack(pady=(8, 0))

    plus_10_button = tk.Button(
        increment_frame,
        text="+10 min",
        width=8,
        command=lambda: handle_time_increment(10),
    )
    plus_10_button.pack(side=tk.LEFT, padx=4)

    plus_1h_button = tk.Button(
        increment_frame,
        text="+1h",
        width=8,
        command=lambda: handle_time_increment(60),
    )
    plus_1h_button.pack(side=tk.LEFT, padx=4)

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