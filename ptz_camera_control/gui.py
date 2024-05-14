import tkinter as tk
from camera_control import pan_left, pan_right, tilt_up, tilt_down, zoom_in, zoom_out, reset_pan, reset_tilt

def start_gui():
    """
    Starts the GUI application for PTZ camera control.
    """
    app = tk.Tk()
    app.title("PTZ Camera Control")

    # Set a common padding for all buttons
    button_padding = {'padx': 20, 'pady': 10}

    frame = tk.Frame(app, padx=20, pady=20)
    frame.pack()

    btn_pan_left = tk.Button(frame, text="Pan Left", command=pan_left)
    btn_pan_left.grid(row=1, column=0, **button_padding)

    btn_pan_right = tk.Button(frame, text="Pan Right", command=pan_right)
    btn_pan_right.grid(row=1, column=2, **button_padding)

    btn_tilt_up = tk.Button(frame, text="Tilt Up", command=tilt_up)
    btn_tilt_up.grid(row=0, column=1, **button_padding)

    btn_tilt_down = tk.Button(frame, text="Tilt Down", command=tilt_down)
    btn_tilt_down.grid(row=2, column=1, **button_padding)

    btn_zoom_in = tk.Button(frame, text="Zoom In", command=zoom_in)
    btn_zoom_in.grid(row=3, column=0, **button_padding)

    btn_zoom_out = tk.Button(frame, text="Zoom Out", command=zoom_out)
    btn_zoom_out.grid(row=3, column=2, **button_padding)

    btn_reset_pan = tk.Button(frame, text="Reset Pan", command=reset_pan)
    btn_reset_pan.grid(row=4, column=0, **button_padding)

    btn_reset_tilt = tk.Button(frame, text="Reset Tilt", command=reset_tilt)
    btn_reset_tilt.grid(row=4, column=2, **button_padding)

    app.mainloop()

# Call the GUI function if running this script directly
if __name__ == "__main__":
    start_gui()
