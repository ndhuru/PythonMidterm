import cv2
import tkinter as tk
import PIL.Image
import PIL.ImageTk


def start_video_stream():
    # Create a VideoCapture object to capture video from the default camera
    cap = cv2.VideoCapture(0)

    # Create a Tkinter window to display the video stream
    video_window = tk.Toplevel()
    video_window.title("Video Stream")

    # Create a label to hold the video stream frames
    video_label = tk.Label(video_window)
    video_label.pack()

    # Function to update the video stream frames
    def update_video_stream():
        ret, frame = cap.read()
        if ret:
            # Convert the frame to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Create a PIL ImageTk object from the frame
            image = PIL.Image.fromarray(frame_rgb)
            image_tk = PIL.ImageTk.PhotoImage(image)

            # Update the label with the new frame
            video_label.configure(image=image_tk)
            video_label.image = image_tk

        # Schedule the next update
        video_label.after(10, update_video_stream)

    # Start updating the video stream frames
    update_video_stream()
