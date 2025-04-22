import os


def get_all_files(directory):
    """
    Retrieves all file paths from a specified directory.
    :param directory: The path to the directory.
    :return: A list of all file paths in the directory.
    """
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def delete_file(file):
    """
    Deletes a file if it exists.
    :param file: The path to the file to delete.
    :return: True if the file was deleted, False otherwise.
    """
    if os.path.exists(file):
        try:
            os.remove(file)
        except:
            return False


def doesfileexist(path):
    """
    Checks if a file exists at the given path.
    :param path: File path to check.
    :return: True if file exists, False otherwise.
    """
    return os.path.isfile(path)