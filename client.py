import tkinter as tk
from tkinter import messagebox
import requests
import sys
import datetime

# API base URL
API_BASE_URL = 'http://localhost:4444'

# Create a list to hold the past four commands
command_log = []

# Variable to store the username of the logged-in user
logged_in_user = ""

# Function to send control command to the API and update the command log
def send_command(command):
    endpoint = f'{API_BASE_URL}/control'
    payload = {'command': command}
    response = requests.post(endpoint, json=payload)
    if response.status_code == 200:
        update_command_log(command)
    else:
        messagebox.showerror("Error", "Failed to execute command.")

# Function to update the command log
def update_command_log(command):
    global logged_in_user
    if len(command_log) == 4:
        command_log.pop(0)
    log_entry = f"{logged_in_user}: {command} on {datetime.datetime.now()}"
    command_log.append(log_entry)
    log_text.set('\n'.join(command_log))
    with open('cmdlog.txt', 'a') as file:
        file.write(log_entry + '\n')

# Function to receive the logged-in username from main.py
def receive_username(username):
    global logged_in_user
    logged_in_user = username

# Create the main window
window = tk.Tk()
window.configure(bg='#639c8f')
window.geometry('900x600')
window.title('Python Client')
window.resizable(False, False)

# Create log label
log_label = tk.Label(window, text='Log History:', bg='#639c8f', fg='#e21d76', font='bold')
log_label.grid(row=15, column=0)

# Create log text widget
log_text = tk.StringVar()
log_text_widget = tk.Label(window, textvariable=log_text, justify='left', anchor='w', relief='solid')
log_text_widget.grid(row=16, column=0, padx=10, pady=10)

# Function to send 'forward' command
def forward_command():
    send_command('forward')

# Function to send 'backward' command
def backward_command():
    send_command('backward')

# Function to send 'left' command
def left_command():
    send_command('left')

# Function to send 'right' command
def right_command():
    send_command('right')

# Function to send 'stop' command
def stop_command():
    send_command('stop')

# Function to send 'start' command
def play_command():
    send_command('play')

# Create arrow buttons
forward_button = tk.Button(window, text='\u2191', command=forward_command, width=5, height=2)
backward_button = tk.Button(window, text='\u2193', command=backward_command, width=5, height=2)
left_button = tk.Button(window, text='\u2190', command=left_command, width=5, height=2)
right_button = tk.Button(window, text='\u2192', command=right_command, width=5, height=2)

# Create stop button
stop_button = tk.Button(window, text='\u26D4', command=stop_command, bg='red', fg='white', width=5, height=2)

# Create start button
start_button = tk.Button(window, text='\u25B6', command=play_command, bg='green', fg='white', width=5, height=2)

# Position the buttons in the window
forward_button.grid(row=4, column=1, padx=10, pady=10)
backward_button.grid(row=6, column=1, padx=10, pady=10)
left_button.grid(row=5, column=0, padx=10, pady=10)
right_button.grid(row=5, column=2, padx=10, pady=10)
stop_button.grid(row=5, column=1, padx=10, pady=10)
start_button.grid(row=7, column=1, padx=10, pady=10)

# Function to handle window close event
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

# Set the closing event handler
window.protocol("WM_DELETE_WINDOW", on_closing)

# Call the receive_username function with the username passed as an argument
if len(sys.argv) > 1:
    receive_username(sys.argv[1])

window.mainloop()
