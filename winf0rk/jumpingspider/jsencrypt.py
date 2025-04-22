import hashlib
import random
import base64
from .jsbasics import *

def derive_key_from_password(password: str, length=32) -> bytes:
    """
    Derives a key from a password using SHA-256.
    :param password: The password to derive the key from.
    :param length: The desired length of the derived key.
    :return: The derived key as bytes.
    """
    return hashlib.sha256(password.encode('utf-8')).digest()[:length]


def encrypt(plain_text: str, password: str) -> str:
    """
    Encrypts a plain text using AES encryption and a password.
    :param plain_text: The text to encrypt.
    :param password: The password to use for encryption.
    :return: The encrypted text as a base64 string.
    """
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import padding
    key = derive_key_from_password(password)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plain_text.encode('utf-8')) + padder.finalize()
    cipher_text = encryptor.update(padded_data) + encryptor.finalize()
    encrypted_data = iv + cipher_text
    return base64.b64encode(encrypted_data).decode('utf-8')


def decrypt(encrypted_base64: str, password: str) -> str:
    """
    Decrypts a base64-encoded encrypted string using AES and a password.
    :param encrypted_base64: The base64-encoded encrypted text.
    :param password: The password used for decryption.
    :return: The decrypted plain text, or None if decryption fails.
    """
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import padding
    try:
        key = derive_key_from_password(password)
        encrypted_data = base64.b64decode(encrypted_base64)
        iv = encrypted_data[:16]
        cipher_text = encrypted_data[16:]
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_padded_data = decryptor.update(cipher_text) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        plain_text = unpadder.update(decrypted_padded_data) + unpadder.finalize()
        return plain_text.decode('utf-8')
    except Exception as e:
        error(f"Error: {e}")


def hash_string(input_string):
    """
    Hashes a string using the SHA-256 algorithm.
    :param input_string: The string to hash.
    :return: The SHA-256 hash of the input string as a hexadecimal string.
    """
    hash_function = 'sha256'
    hash_obj = hashlib.new(hash_function)
    hash_obj.update(input_string.encode('utf-8'))
    return hash_obj.hexdigest()


def genrandomkey(charnum, chars):
    """
    Generates a random key consisting of specified characters and length.
    :param charnum: Number of characters in the key.
    :param chars: String containing characters to choose from.
    :return: Randomly generated key as a string.
    """
    return ''.join(random.choice(chars) for _ in range(charnum))