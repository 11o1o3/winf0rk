import sys
import os

def arguments():
    """
    Retrieves the command-line arguments passed to the script.
    :return: A list of arguments passed to the script.
    """
    return sys.argv


def commandlineoutput(command):
    """
    Executes a command in the shell and returns its output.
    :param command: The shell command to execute.
    :return: The output of the command as a string.
    """
    return os.popen(command).read().replace("\n", "").replace("   ", "").replace(" ", "")

