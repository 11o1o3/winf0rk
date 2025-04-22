import base64


def to_base64(input_string: str) -> str:
    """
    Encodes a string to Base64.
    :param input_string: The string to encode.
    :return: Base64 encoded string.
    """
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    return encoded_bytes.decode('utf-8')


def from_base64(encoded_string: str) -> str:
    """
    Decodes a Base64 encoded string.
    :param encoded_string: The Base64 encoded string.
    :return: Decoded string.
    """
    decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))
    return decoded_bytes.decode('utf-8')


def file_from_base64(input_file_path: str, output_file_path: str):
    """
    Decodes a Base64 encoded file and writes the output to a new file.
    :param input_file_path: Path to the Base64 encoded file.
    :param output_file_path: Path where the decoded file should be saved.
    """
    with open(input_file_path, 'rb') as file:
        decoded_bytes = base64.b64decode(file.read())
    with open(output_file_path, 'wb') as file:
        file.write(decoded_bytes)


def file_to_base64(file):
    """
    Converts a file to a base64-encoded string.
    :param file: The path to the file.
    :return: The base64-encoded content of the file.
    """
    with open(file, "rb") as f:
        file_content = f.read()
    return base64.b64encode(file_content).decode('utf-8')


def base64tofile(base64_string, output_file):
    """
    Converts a base64-encoded string back into a file.
    :param base64_string: The base64-encoded string.
    :param output_file: The path to save the decoded file.
    """
    file_content = base64.b64decode(base64_string)
    with open(output_file, "wb") as f:
        f.write(file_content)
