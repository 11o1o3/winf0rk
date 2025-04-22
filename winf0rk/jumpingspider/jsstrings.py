import sys

def string_to_array(string):
    """
    Converts a string into an array of words.
    :param string: The string to convert.
    :return: A list of words.
    """
    return string.split()


def string_to_fixed_lenght(string, lenght=32):
    """
    Converts a string to a fixed length by truncating or padding it.
    :param string: The string to modify.
    :param lenght: The desired length of the string.
    :return: The modified string.
    """
    string = str(string)
    if len(string) > lenght:
        return string[0:lenght]
    else:
        while len(string) < lenght:
            string = string + string
        return string[0:lenght]


def arguments_contains(key):
    """
    Checks if a command-line argument contains a specific key.
    :param key: The key to look for.
    :return: True if the key is found in the command-line arguments, False otherwise.
    """
    output = False
    for i in sys.argv:
        if i.lower() == key.lower():
            output = True
    return output


def arguments_index(key):
    """
    Finds the value of a command-line argument by key.
    :param key: The key to search for in the command-line arguments.
    :return: The argument's value if found, None otherwise.
    """
    output = None
    if arguments_contains(key):
        for i in sys.argv:
            if i.lower() == key.lower():
                output = i
    return output


def array_contains(array, key):
    """
    Checks if a key exists in an array.
    :param array: The list to search in.
    :param key: The key to look for.
    :return: True if the key exists in the array, False otherwise.
    """
    output = False
    for i in array:
        if i == key:
            output = True
    return output


def array_index(array, key):
    """
    Finds the index of a key in an array.
    :param array: The list to search in.
    :param key: The key to find the index of.
    :return: The index of the key if found, None otherwise.
    """
    output = None
    for i in range(len(array)):
        if array[i - 1] == key:
            output = i - 1
    return int(output)