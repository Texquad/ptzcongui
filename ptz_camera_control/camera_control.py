import subprocess

# Define the path to the video device
VIDEO_DEVICE = '/dev/video2'  # Update this if your device has a different path

def control_camera(command, value):
    """
    Controls the PTZ camera by setting the specified control to the given value.
    
    Args:
        command (str): The control command (e.g., 'pan_relative', 'tilt_relative').
        value (int): The value to set for the control.
    """
    print(f'Setting {command} to {value}')
    result = subprocess.run(['v4l2-ctl', '--device', VIDEO_DEVICE, '--set-ctrl', f'{command}={value}'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")
        new_value = get_control_value(command)
        print(f"New value of {command} is {new_value}")

def get_control_value(control):
    """
    Gets the current value of a control.
    
    Args:
        control (str): The control command (e.g., 'zoom_absolute').
    
    Returns:
        int: The current value of the control.
    """
    result = subprocess.run(['v4l2-ctl', '--device', VIDEO_DEVICE, '--get-ctrl', control], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return 0
    value = int(result.stdout.split(': ')[1].strip())
    print(f"Current value of {control} is {value}")
    return value

# Constants for control values
PAN_STEP = 100  # Adjust as necessary
TILT_STEP = 100  # Adjust as necessary
ZOOM_STEP = 10

def pan_left():
    control_camera('pan_relative', -PAN_STEP)

def pan_right():
    control_camera('pan_relative', PAN_STEP)

def tilt_up():
    control_camera('tilt_relative', -TILT_STEP)  # Check direction

def tilt_down():
    control_camera('tilt_relative', TILT_STEP)  # Check direction

def zoom_in():
    current_zoom = get_control_value('zoom_absolute')
    control_camera('zoom_absolute', min(1000, current_zoom + ZOOM_STEP))  # Adjusted direction

def zoom_out():
    current_zoom = get_control_value('zoom_absolute')
    control_camera('zoom_absolute', max(100, current_zoom - ZOOM_STEP))  # Adjusted direction

def reset_pan():
    control_camera('pan_reset', 1)

def reset_tilt():
    control_camera('tilt_reset', 1)
