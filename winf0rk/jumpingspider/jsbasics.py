import os
import threading
from .jscolor import *
import datetime

def helloworld():
    """
    A simple test function that returns True.
    :return: True.
    """
    return True


def daemon(function):
    """
    Returns a background thread (daemon) for a given function.
    :param function: The function to execute in the background.
    :return: A daemon thread.
    """
    deamon = threading.Thread(target=function, daemon=True)
    return deamon

def error(errormessage="Unexpected error!"):
    """
    Raises an error with the given message.
    :param errormessage: The error message to raise.
    """
    raise ValueError(errormessage)

def appdata_path():
    """
    Retrieves the path to the application's data directory.
    :return: The path to the APPDATA environment variable.
    """
    return os.getenv('APPDATA')


def log(content, state=0, printout=True, save=False, path=""):
    """
    Creates a log entry and optionally prints or saves it.
    :param content: The content to log.
    :param state: The severity level of the log (0=info, 1=warning, 2=error).
    :param printout: Whether to print the log to the console.
    :param save: Whether to save the log to a file.
    :param path: The path to the log file (required if save is True).
    """
    if save == True and path == "":
        raise ValueError("No path to log file given")
    else:
        display_states = {0: "[INFO]", 1: "[WARNING]", 2: "[ERROR]"}
        displaystate = display_states.get(state, "[INFO]")
        logdate = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_entry = f"{logdate} {displaystate} {content}\n"
        if save:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "a", encoding="utf-8") as file:
                file.write(log_entry)
        if printout:
            if state == 1:
                print(rgb_text(log_entry, 0, 0, 0, 255, 255, 0))
            elif state == 2:
                print(rgb_text(log_entry, 0, 0, 0, 255, 0, 0))
            else:
                print(rgb_text(log_entry, 0, 0, 0, 0, 255, 0))


def download_file(url, save_path):
    import urllib.request
    """
    Downloads a file from a given URL and saves it to the specified path.
    :param url: The URL of the file to download.
    :param save_path: The local file path where the downloaded file should be saved.
    :return: True if the file was downloaded successfully, False otherwise.
    """
    try:
        with urllib.request.urlopen(url) as response, open(save_path, 'wb') as file:
            while chunk := response.read(1024):
                file.write(chunk)
        return True
    except Exception as e:
        raise ValueError(f"error: {e}")