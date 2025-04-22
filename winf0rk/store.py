import jumpingspider as js

store_file = "winf0rk_store.txt"

def save(key, value):
    return js.config_save(store_file, key, value)

def read(key):
    return js.config_read(store_file, key)