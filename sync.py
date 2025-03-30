import os
import time
import socket
from datetime import datetime

def check_network():
    try:
        socket.create_connection(("www.github.com", 80), timeout=5)
        return True
    except socket.error:
        return False

if check_network():
    time.sleep(60)
    os.system("git remote add origin git@github.com:canmi21/uptime.git")
    os.system("git branch -M main")
    os.system("git add .")
    commit_message = "Sync: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.system(f"git commit -m \"{commit_message}\"")
    os.system("git push -u origin main")
