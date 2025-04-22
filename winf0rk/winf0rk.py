import jumpingspider as js

js.start_timer("importtime")

import time
import store
import colorbar
from color import coloredstring as colored
import getinfos
import logo
import graphs

processbarlenght = 21
drive = "C"
delay = 0.15

def defcolor(string):
    return colored(string, 100, 100, 200)

importtime =js.stop_timer("importtime")
js.start_timer("printout")

print("")
print(logo.getlogo(0) + defcolor(getinfos.info_username()) + "@" + defcolor(getinfos.get("info_hostname")))
print(logo.getlogo(1) + graphs.line(len(getinfos.info_hostname() + "@" + getinfos.get("info_username"))))
print(logo.getlogo(2) + defcolor("Logged into: ") + getinfos.get("info_domain"))
print(logo.getlogo(3) + defcolor("Serial Number: ") + getinfos.get("info_serialnumber"))
print(logo.getlogo(4) + defcolor("Uptime: ") + getinfos.info_uptime())
print(logo.getlogo(5) + defcolor("CPU: ") + getinfos.get("info_cpu"))
print(logo.getlogo(6)  + defcolor("GPU: ") + getinfos.get("info_gpu"))
print(logo.getlogo(7) + defcolor("Local IP: ") + getinfos.info_ip())
print(logo.getlogo(8) + defcolor("MAC: ") + getinfos.get("info_mac"))
print(logo.getlogo(9) + defcolor("Memory:        ") + graphs.processbar(getinfos.info_used_ram(), getinfos.info_total_ram(), processbarlenght) + " " + str(getinfos.info_used_ram()) + "GB / " + str(getinfos.info_total_ram()) + "GB ")
print(logo.getlogo(10) + defcolor("Storage (" + drive + r":\): ") + graphs.processbar(getinfos.info_storage_usedsize(drive), getinfos.info_storage_totalsize(drive), processbarlenght) + " " + str(getinfos.info_storage_usedsize(drive)) + " / " + str(getinfos.info_storage_totalsize(drive)))
print(logo.getlogo(11))
print(logo.getlogo(12) + colorbar.colorbar_dark)
print(logo.getlogo(13) + colorbar.colorbar_light)
print(logo.getlogo(14))
print("")

printouttime = js.stop_timer("printout")
if js.arguments_contains("-t") or js.arguments_contains("/t"):
    print("Import time: " + str(importtime) + "ms")
    print("Readout time: " + str(printouttime) + "ms")
    print("")

if js.arguments_contains("-r") or js.arguments_contains("/r"):
    js.delete_file(store.store_file)

time.sleep(delay)