# ptz_camera_control/camera_control.py

import subprocess

def control_camera(command, value):
    """
    Controls the PTZ camera by setting the specified control to the given value.
    
    Args:
        command (str): The control command (e.g., 'pan_absolute', 'tilt_absolute').
        value (int): The value to set for the control.
    """
    subprocess.run(['v4l2-ctl', '--set-ctrl', f'{command}={value}'])

def pan_left():
    control_camera('pan_absolute', -1000)

def pan_right():
    control_camera('pan_absolute', 1000)

def tilt_up():
    control_camera('tilt_absolute', -1000)

def tilt_down():
    control_camera('tilt_absolute', 1000)

def zoom_in():
    control_camera('zoom_absolute', 200)

def zoom_out():
    control_camera('zoom_absolute', 0)