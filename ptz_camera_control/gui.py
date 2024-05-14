# ptz_camera_control/gui.py

import tkinter as tk
from .camera_control import pan_left, pan_right, tilt_up, tilt_down, zoom_in, zoom_out

def start_gui():
    """
    Starts the GUI application for PTZ camera control.
    """
    app = tk.Tk()
    app.title("PTZ Camera Control")

    btn_pan_left = tk.Button(app, text="Pan Left", command=pan_left)
    btn_pan_left.pack(pady=5)

    btn_pan_right = tk.Button(app, text="Pan Right", command=pan_right)
    btn_pan_right.pack(pady=5)

    btn_tilt_up = tk.Button(app, text="Tilt Up", command=tilt_up)
    btn_tilt_up.pack(pady=5)

    btn_tilt_down = tk.Button(app, text="Tilt Down", command=tilt_down)
    btn_tilt_down.pack(pady=5)

    btn_zoom_in = tk.Button(app, text="Zoom In", command=zoom_in)
    btn_zoom_in.pack(pady=5)

    btn_zoom_out = tk.Button(app, text="Zoom Out", command=zoom_out)
    btn_zoom_out.pack(pady=5)

    app.mainloop()