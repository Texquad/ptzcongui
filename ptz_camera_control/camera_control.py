import subprocess

# Define the path to the video device
VIDEO_DEVICE = '/dev/video2'  # Update this if your device has a different path

def control_camera(command, value):
    print(f'Setting {command} to {value}')
    result = subprocess.run(['v4l2-ctl', '--device', VIDEO_DEVICE, '--set-ctrl', f'{command}={value}'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")
        new_value = get_control_value(command)
        print(f"New value of {command} is {new_value}")

def get_control_value(control):
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
    print("Attempting to tilt up using tilt_relative...")
    control_camera('tilt_relative', TILT_STEP)

def tilt_down():
    print("Attempting to tilt down using tilt_relative...")
    control_camera('tilt_relative', -TILT_STEP)

def zoom_in():
    current_zoom = get_control_value('zoom_absolute')
    control_camera('zoom_absolute', min(1000, current_zoom + ZOOM_STEP))

def zoom_out():
    current_zoom = get_control_value('zoom_absolute')
    control_camera('zoom_absolute', max(100, current_zoom - ZOOM_STEP))

def reset_pan():
    control_camera('pan_reset', 1)

def reset_tilt():
    control_camera('tilt_reset', 1)

# Function to test tilt commands
def test_tilt():
    print("Testing tilt_relative up...")
    control_camera('tilt_relative', 100)
    control_camera('tilt_relative', -100)

# Call the test function if running this script directly
if __name__ == "__main__":
    test_tilt()
