# __init__.py
"""
Jumping Spider - A small collection of Python utility functions.

This module provides a structured set of functions across different categories:

Modules & Functions:

# Time Management (jstime.py)
- start_timer(name): Starts a timer with the given name.
- get_timer_state(name): Retrieves the elapsed time of a running timer in milliseconds.
- stop_timer(name): Stops a timer and returns the elapsed time in milliseconds.

# Color Formatting (jscolor.py)
- rgb_color_text(text, r, g, b): Formats text with the specified RGB foreground color for terminal output.
- rgb_bg_text(text, r, g, b): Formats text with the specified RGB background color for terminal output.
- rgb_text(text, fg_r, fg_g, fg_b, bg_r, bg_g, bg_b): Formats text with both foreground and background RGB colors for terminal output.

# Base64 Encoding/Decoding (jsbase64.py)
- to_base64(input_string): Encodes a string to Base64.
- from_base64(encoded_string): Decodes a Base64 string.
- file_to_base64(file): Converts a file to a base64-encoded string.
- file_from_base64(input_file_path, output_file_path): Decodes a Base64 encoded file and writes the output to a new file.
- base64tofile(base64_string, output_file): Converts a Base64 string back to a file.

# Basic tasks (jsbasics.py)
- helloworld(): returns True
- daemon(function): Returns a background thread (daemon) for a given function.
- error(errormessage): Raises an error with the given message.
- genrandomkey(charnum, chars): Generates a random key of specified length.
- appdata_path(): Retrieves the path to the application's data directory.
- log(content, state, printout, save, path): Creates a log entry and optionally prints or saves it.
- download_file(url, save_path): Downloads a file from a given URL and saves it to the specified path.

# File Operations (jsfiles.py)
- doesfileexist(path): Checks if a file exists at the given path.
- delete_file(file): Deletes a file if it exists.
- get_all_files(directory): Retrieves all file paths from a specified directory.

# Configuration Management (jsconfig.py)
- ensure_config_path_exists(config_file): Ensures the configuration directory exists.
- config_save(config_file, key, content): Saves a key-value pair to config file.
- config_read(config_file, key): Reads a value from config file.
- does_exist_in_config(config_file, key): Checks if a key exists in config file.
- delete_from_config(config_file, key): Deletes a key from config file.
- get_all_config_entries(config_file): Retrieves all key-value pairs from config.

# Command-Line Argument Handling (jscommandline.py)
- arguments(): Returns command-line arguments.
- arguments_contains(key): Checks if an argument exists.
- arguments_index(key): Finds argument value by key.
- commandlineoutput(command): Runs a shell command and returns output.

# Encryption (jsencrypt.py)
- derive_key_from_password(password: str, length=32): Derives a key from password.
- encrypt(plain_text, password): Encrypts text using AES.
- decrypt(encrypted_base64, password): Decrypts AES-encrypted text.

# Miscellaneous (jsmiscellaneous.py)
- helloworld(): Returns True (test function).
- run_in_background(function): Runs a function in a background thread.
- daemon(function): Returns a daemon thread for a function.
- string_to_array(string): Splits a string into an array.
- string_to_fixed_lenght(string, length=32): Converts a string to fixed length.

# Environment Detection (jsmiscellaneous.py)
- is_running_in_vm(): Detects if running inside a virtual machine.
- is_running_in_sandbox(): Detects if running inside a sandbox/container.

"""

from .jstime import *
start_timer("jumpingspider")
start_timer("importtime")

from .jsbase64 import *
from .jsbasics import *
from .jscolor import *
from .jscommandline import *
from .jsconfig import *
from .jsencrypt import *
from .jsfiles import *
from .jsmiscellaneous import *
from .jsstrings import *

importtime = stop_timer("importtime")

def jumpingspider():
    runtime = stop_timer("jumpingspider")
    print("")
    print("---" + rgb_color_text("Jumping Spider", 255, 150, 255) + "---" + rgb_color_text("v 1.9.4", 255, 150,255) + "-----------")
    print("A small collection of python functions")
    print("")
    if runtime == importtime:
        print("Total time to load: " + str(runtime) + "ms")
    else:
        print("Time to load: " + str(runtime) + "ms, import only " + str(importtime) + "ms")
    print("")

__call__ = jumpingspider

if __name__ == "__main__":
    jumpingspider()