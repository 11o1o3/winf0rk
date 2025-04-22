import os
import subprocess
import pyautogui


def is_running_in_vm() -> bool:
    """
    Checks if the script is running inside a virtual machine.
    :return: True if the script is running in a VM, False otherwise.
    """
    try:
        if os.name == 'nt':  # Windows
            output = subprocess.check_output('wmic bios get serialnumber', shell=True).decode().lower()
            if any(keyword in output for keyword in ['vmware', 'virtual', 'qemu', 'vbox']):
                return True
        else:  # Linux & Mac
            output = subprocess.check_output('systemd-detect-virt', shell=True).decode().strip().lower()
            if output not in ['none', '']:
                return True
    except:
        pass
    return False


def is_running_in_sandbox() -> bool:
    """
    Checks if the script is running inside a sandbox or container.
    :return: True if the script is running in a sandbox, False otherwise.
    """
    sandbox_indicators = [
        '/run/.containerenv',  # Podman
        '/.dockerenv',  # Docker
        '/proc/1/cgroup',  # Docker/LXC
        '/sys/fs/selinux',  # Sandboxes mit SE Linux
    ]
    # Check for files/paths that indicate containerization
    for path in sandbox_indicators:
        if os.path.exists(path):
            return True
    # Check for common container/sandbox process names in cgroup (Linux)
    try:
        with open('/proc/1/cgroup', 'r') as f:
            cgroup_content = f.read().lower()
            if any(term in cgroup_content for term in ['docker', 'lxc', 'kubepods']):
                return True
    except Exception:
        pass
    return False




def get_mouse_position():
    """
    Retrieves the current position of the mouse cursor on the screen.
    :return: A tuple (x, y) representing the current mouse coordinates.
    """
    return pyautogui.position()


def set_mouse_position(x, y):
    """
    Moves the mouse cursor to the specified position on the screen.
    :param x: The horizontal coordinate (in pixels from the left edge of the screen).
    :param y: The vertical coordinate (in pixels from the top edge of the screen).
    :return: None
    """
    pyautogui.moveTo(x, y)