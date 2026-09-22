import subprocess  # let us run external program from python
import time
import tkinter as tk
from tkinter import messagebox

FOCUS_SECONDS = 3 * 60 * 60
BREAK_SECONDS = 60 * 60
ALARM_SOUND_PATH = "/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga"
ALARM_REPEAT_COUNT = 3

def launch_startup_applications():
    """Launch the desired application when PC is turned on"""
    apps = [
        "code",
        "brave-browser https://open.spotify.com/",
        "brave-browser https://blackboard.salford.ac.uk/ultra/course",
        "gnome-terminal",
    ]

    for app in apps:
        try:
            subprocess.Popen(app, shell=True)
            print(f"Launched {app}")
            time.sleep(1)
        except Exception as error:
            print(f"Failed to launch {app}: {error}")

    start_focus_timer_window()

def formatSecondsAsClockText(total_seconds):
    """Return seconds as HH:MM:SS"""
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def playAlarmSoundRepeatedly(repeat_count=ALARM_REPEAT_COUNT):
    """Play the system alarm sound a number of times"""
    for _ in range(repeat_count):
        try:
            subprocess.run(["paplay", ALARM_SOUND_PATH], check=True)
        except Exception as error:
            print(f"Failed to play alarm sound: {error}")
            return

def start_focus_timer_window():
    """Three hour focus session, 15 minute break, then a restart prompt"""
    root = tk.Tk()
    root.title("Focus Session")
    root.geometry("900x400")
    root.configure(bg="#2c3e50")

    clock_label = tk.Label(root, text="", font=("Arial", 54, "bold"), fg="#3498db", bg="#2c3e50")
    clock_label.pack(pady=20)

    status_label = tk.Label(root, text="Focus Time", font=("Arial", 24), fg="#27ae60", bg="#2c3e50")
    clock_label.pack(pady=20)

    status_label = tk.Label(root, text="Focus Time", font=("Arial", 24), fg="#27ae60", bg="#2c3e50")
    status_label.pack()

    def countdown_then_call(seconds_left, on_finished):
        clock_label.config(text=formatSecondsAsClockText(seconds_left))
        if seconds_left <= 0:
            on_finished()
            return
        root.after(1000, countdown_then_call, seconds_left - 1, on_finished)

    def start_break_countdown():
        status_label.config(text="Break Time", fg="#e67e22")
        playAlarmSoundRepeatedly()
        messagebox.showinfo("Focus complete", "Three hours done. Take a 1 hour break.")
        countdown_then_call(BREAK_SECONDS, ask_to_restart_focus_session)

    def ask_to_restart_focus_session():
        playAlarmSoundRepeatedly()
        wants_another = messagebox.askyesno("Break over", "Start another 3 hour focus session?")
        if wants_another:
            status_label.config(text="Focus Time", fg="#27ae60")
            countdown_then_call(FOCUS_SECONDS, start_break_countdown)
        else:
            root.destroy()
    countdown_then_call(FOCUS_SECONDS, start_break_countdown)
    root.mainloop()

if __name__ == "__main__":
    launch_startup_applications()