import os

def ensure_config_path_exists(config_file):
    """
    Ensures that the directory for a given configuration file exists.
    :param config_file: Path to the configuration file.
    """
    folder = os.path.dirname(config_file)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)


def config_save(config_file, key, content):
    """
    Saves a key-value pair to a configuration file.
    :param config_file: The path to the configuration file.
    :param key: The key to store.
    :param content: The content associated with the key.
    """
    ensure_config_path_exists(config_file)
    config = {}
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            for line in f:
                if '=' in line:
                    k, v = line.strip().split('=', 1)
                    config[k] = v
    if config.get(key) != content:
        config[key] = content
        with open(config_file, 'w') as f:
            for k, v in config.items():
                f.write(f"{k}={v}\n")


def config_read(config_file, key):
    """
    Reads a value from a configuration file.
    :param config_file: The path to the configuration file.
    :param key: The key to look up.
    :return: The value associated with the key, or None if not found.
    """
    ensure_config_path_exists(config_file)
    if not os.path.exists(config_file):
        with open(config_file, 'w') as f:
            return None
    with open(config_file, 'r') as f:
        for line in f:
            if '=' in line:
                k, v = line.strip().split('=', 1)
                if k == key:
                    return v
    return None


def does_exist_in_config(config_file, key):
    """
    Checks if a key exists in the configuration file.
    :param config_file: The path to the configuration file.
    :param key: The key to check for.
    :return: True if the key exists, False otherwise.
    """
    ensure_config_path_exists(config_file)
    if config_read(config_file, key) is None:
        return False
    else:
        return True


def config_does_exist(config_file, key):
    """
    Checks if a key exists in the configuration file and creates the file if it doesn't exist.
    :param config_file: The path to the configuration file.
    :param key: The key to check for.
    :return: True if the key exists, False otherwise. Creates the file if it doesn't exist.
    """
    ensure_config_path_exists(config_file)
    if not os.path.exists(config_file):
        with open(config_file, 'w') as f:
            return False
    with open(config_file, 'r') as f:
        for line in f:
            if '=' in line:
                k, _ = line.strip().split('=', 1)
                if k == key:
                    return True
    return False


def delete_from_config(config_file, key):
    """
    Deletes a key-value pair from the configuration file.
    :param config_file: The path to the configuration file.
    :param key: The key to be deleted.
    :return: True if the key was successfully deleted, False otherwise.
    """
    ensure_config_path_exists(config_file)
    if not os.path.exists(config_file):
        return False
    config = {}
    with open(config_file, 'r') as f:
        for line in f:
            if '=' in line:
                k, v = line.strip().split('=', 1)
                config[k] = v
    if key not in config:
        return False
    del config[key]
    with open(config_file, 'w') as f:
        for k, v in config.items():
            f.write(f"{k}={v}\n")
    return True


def get_all_config_entries(config_file):
    """
    Retrieves all key-value entries from the configuration file.
    :param config_file: The path to the configuration file.
    :return: A list of strings containing all the key-value pairs.
    """
    ensure_config_path_exists(config_file)
    entries = []
    if not os.path.exists(config_file):
        return entries
    with open(config_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if '=' in line:
                entries.append(line)
    return entries
