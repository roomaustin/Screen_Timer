import tkinter as tk
import time

# Set the threshold for screen time (in seconds)
SCREEN_TIME_THRESHOLD = 3600  # e.g., 1 hour

def update_time():
    global screen_time
    screen_time += 1
    time_label.config(text=f"Screen Time: {screen_time} seconds")

    if screen_time >= SCREEN_TIME_THRESHOLD:
        reminder_label.config(text="It's time to take a break!")

    root.after(1000, update_time)

def reset_screen_time():
    global screen_time
    screen_time = 0
    time_label.config(text="Screen Time: 0 seconds")
    reminder_label.config(text="")

root = tk.Tk()
root.title("Screen Time Reminder")

screen_time = 0

time_label = tk.Label(root, text="Screen Time: 0 seconds")
time_label.pack()

reminder_label = tk.Label(root, text="")
reminder_label.pack()

reset_button = tk.Button(root, text="Reset Screen Time", command=reset_screen_time)
reset_button.pack()

update_time()
root.mainloop()
