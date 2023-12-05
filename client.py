import tkinter as tk
import requests


# API base URL
API_BASE_URL = 'http://localhost:4444'

# Create a list to hold the past four commands
command_log = []

# Function to send control command to the API and update the command log
def send_command(command):
    endpoint = f'{API_BASE_URL}/control'
    payload = {'command': command}
    response = requests.post(endpoint, json=payload)
    if response.status_code == 200:
        print('Command executed successfully.')
        print(command + " " + "executed")
        update_command_log(command)
    else:
        print('Error executing command.')

# Function to update the command log
def update_command_log(command):
    if len(command_log) == 4:
        command_log.pop(0)
    command_log.append(command)
    log_text.set('\n'.join(command_log))

# Create the main window
window = tk.Tk()
window.title('Robot Control')

# Set the window size
window.geometry('900x600')

# Create log label
log_label = tk.Label(window, text='Command Log')
log_label.grid(row=4, column=1, padx=10, pady=10)

# Create log text widget
log_text = tk.StringVar()
log_text_widget = tk.Label(window, textvariable=log_text, justify='left', anchor='w', relief='solid')
log_text_widget.grid(row=5, column=1, padx=10, pady=10)

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

# Function to send 'play' command
def play_command():
    send_command('play')

# Create arrow buttons
forward_button = tk.Button(window, text='\u2191', command=forward_command, width=5, height=2)
backward_button = tk.Button(window, text='\u2193', command=backward_command, width=5, height=2)
left_button = tk.Button(window, text='\u2190', command=left_command, width=5, height=2)
right_button = tk.Button(window, text='\u2192', command=right_command, width=5, height=2)

# Create stop button
stop_button = tk.Button(window, text='\u2B22', command=stop_command, bg='red', fg='white', width=5, height=2)

# Create play button
play_button = tk.Button(window, text='\u25B6', command=play_command, bg='green', fg='white', width=5, height=2)

# Position the buttons in the window
forward_button.grid(row=0, column=1, padx=10, pady=10)
backward_button.grid(row=2, column=1, padx=10, pady=10)
left_button.grid(row=1, column=0, padx=10, pady=10)
right_button.grid(row=1, column=2, padx=10, pady=10)
stop_button.grid(row=1, column=1, padx=10, pady=10)
play_button.grid(row=3, column=1, padx=10, pady=10)

window.mainloop()
