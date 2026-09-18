import subprocess # let us run external program from python
import time 
import os # interact with the OS 
import tkinter as tk
from tkinter import messagebox

def launch_apps():
    """Launch the desired application when PC is turned on"""
    apps = [
        "code",
        "brave https://open.spotify.com/?flow_ctx=3483a5d1-d242-4908-9695-fbb858259dfe%3A1789760722",
        "brave https://blackboard.salford.ac.uk/ultra/course", 
        "gnome-terminal"
    ]

    # Launch each application
    for app in apps:
        try:
            subprocess.Popen(app, shell=True)
            print(f"Launched {app}")
            time.sleep(1)
        except Exception as e:
            print("Failed to lanuch {app}")

    # Launch two our focus timer 
    launch_python_timer()

def launch_python_timer():
    """Two hour timer with 15 min break and restart prompt"""
    
    def run_focus_session():
        "Run two hour focus session"
        
        root = tk.Tk()
        root.title("YO MAN YOU READY? LET'S FOCUS FOR 2 FREAKING HOUR")
        root.geometry("1920x800")
        root.configure(bg="#2c3e51")

        time_left = 2 * 60 * 60 # Two hours in second? 
        
        label = tk.Label(root, text="", font=("Arial", 54, "bold"), fg="#3498db", bg="#2c3e50")
        label.pack(pady=20) # make the label visible and pady means padding on the y axis 

        status = tk.Label(root, text="Focus Time", font=("Arial", 24), fg="#27ae60", bg="#2c3e50")
        status.pack()

        

