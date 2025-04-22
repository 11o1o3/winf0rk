import os
import ctypes
import platform
import subprocess
import psutil
import socket
import getmac
import jumpingspider as js
import store

def get(information_name):
    func = globals()[information_name]
    if store.read(information_name) is None:
        store.save(information_name, func())
        return store.read(information_name)
    else:
        def save():
            value = func()
            store.save(information_name, value)
        js.daemon(save).start()
        return store.read(information_name)

def commandlineoutput(command):
    return os.popen(command).read().replace("\n", "").replace("	", "").replace(" ", "")


def commandlineoutputraw(command):
    return os.popen(command).read().replace("\n", "")


def info_mac():
    return getmac.get_mac_address()


def info_username():
    return os.getlogin()


def info_hostname():
    return os.getenv('COMPUTERNAME', 'defaultValue')


def info_serialnumber():
    return "not available"
    # return str(commandlineoutput("wmic bios get serialnumber")[12:])


def info_uptime():
    lib = ctypes.windll.kernel32
    t = lib.GetTickCount64()
    t = int(str(t)[:-3])
    minutes, sec = divmod(t, 60)
    hour, minutes = divmod(minutes, 60)
    days, hour = divmod(hour, 24)
    if days == 0:
        return f"{hour} hours {minutes} minutes"
    else:
        return f"{days} days, {hour} hours {minutes} minutes"


def info_cpu():
    return platform.processor()


def info_gpu():
    try:
        result = subprocess.run(
            ["powershell", "-Command", "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error:: {e}"


def info_ip():
    local_hostname = socket.gethostname()
    ip_addresses = socket.gethostbyname_ex(local_hostname)[2]
    filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]
    first_ip = filtered_ips[:1]
    return first_ip[0]


def info_domain():
    domain = (commandlineoutputraw("whoami"))
    domain = domain[:len(domain) - len(info_username()) - 1]
    return domain

def info_used_ram():
    used = psutil.virtual_memory().percent / 100
    return round(info_total_ram() * used, 1)

def info_total_ram():
    rambyte = psutil.virtual_memory().total
    return round(rambyte / (1024 * 1024 * 1024), 1)

def info_storage_totalsize(drive):
    return round(psutil.disk_usage(drive + ':').total / 2 ** 30, 2)

def info_storage_usedsize(drive):
    return round(psutil.disk_usage(drive + ':').used / 2 ** 30, 2)