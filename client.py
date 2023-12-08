import tkinter as tk
from tkinter import ttk, messagebox
import requests
import sys
import datetime

# api base url
api_base_url = 'http://localhost:4444'

# create a list to hold the past four commands
command_log = []

# variable to store the username of the logged-in user
logged_in_user = ""

# function to send control command to the api and update the command log
def send_command(command):
    endpoint = f'{api_base_url}/control'
    payload = {'command': command}
    response = requests.post(endpoint, json=payload)
    if response.status_code == 200:
        update_command_log(command)
    else:
        messagebox.showerror("Error", "Failed to execute command.")

# function to update the command log
def update_command_log(command):
    global logged_in_user
    if len(command_log) == 4:
        command_log.pop(0)
    log_entry = f"{logged_in_user}: {command} on {datetime.datetime.now()}"
    command_log.append(log_entry)
    log_text.set('\n'.join(command_log))
    with open('cmdlog.txt', 'a') as file:
        file.write(log_entry + '\n')

# function to receive the logged-in username from main.py
def receive_username(username):
    global logged_in_user
    logged_in_user = username

# create the main window
window = tk.Tk()
window.configure(bg='#639c8f')
window.geometry('900x600')
window.title('Python Client')
window.resizable(False, False)

# Create ttk.Separator for horizontal grid line
ttk.Separator(window, orient='horizontal').grid(row=8, column=0, columnspan=17, sticky='ew', pady=10)

# Create ttk.Separator for vertical grid line
ttk.Separator(window, orient='vertical').grid(row=0, column=2, rowspan=17, sticky='ns', padx=10)

# create log label
log_label = tk.Label(window, text='Log History:', bg='#639c8f', fg='#e21d76', font='bold')
log_label.grid(row=9, column=3, padx=10, pady=10, sticky='w')

# create log text widget
log_text = tk.StringVar()
log_text_widget = tk.Label(window, textvariable=log_text, justify='left', anchor='w', relief='solid')
log_text_widget.grid(row=10, column=3, padx=10, pady=10, rowspan=6, sticky='nsew')

# function to send 'forward' command
def forward_command():
    send_command('forward')

# function to send 'backward' command
def backward_command():
    send_command('backward')

# function to send 'left' command
def left_command():
    send_command('left')

# function to send 'right' command
def right_command():
    send_command('right')

# function to send 'stop' command
def stop_command():
    send_command('stop')

# function to send 'start' command
def play_command():
    send_command('play')

# create arrow buttons
forward_button = tk.Button(window, text='\u2191', command=forward_command, width=5, height=2)
backward_button = tk.Button(window, text='\u2193', command=backward_command, width=5, height=2)
left_button = tk.Button(window, text='\u2190', command=left_command, width=5, height=2)
right_button = tk.Button(window, text='\u2192', command=right_command, width=5, height=2)

# create stop button
stop_button = tk.Button(window, text='\u26D4', command=stop_command, bg='red', fg='white', width=5, height=2)

# create start button
start_button = tk.Button(window, text='\u25B6', command=play_command, bg='green', fg='white', width=5, height=2)

# position the buttons in the window
forward_button.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
backward_button.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')
left_button.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
right_button.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')
stop_button.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
start_button.grid(row=4, column=1, padx=10, pady=10, sticky='nsew')

# configure row and column weights for resizing
window.grid_rowconfigure(10, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(3, weight=1)

# function to handle window close event
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

# set the closing event handler
window.protocol("WM_DELETE_WINDOW", on_closing)

# call the receive_username function with the username passed as an argument
if len(sys.argv) > 1:
    receive_username(sys.argv[1])

window.mainloop()
