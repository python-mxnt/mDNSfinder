import socket
import time
import subprocess

hostnameinput = input('What is the Hostname? ') 
print()
mDNSdomain = input('What is your mDNS domain?')
print()

HOSTNAME = hostnameinput + mDNSdomain

def get_ip(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None

def is_reachable(ip):
    try:
        # Cross-platform ping: Windows (-n), Linux/macOS (-c)
        param = "-n" if subprocess.os.name == "nt" else "-c"
        result = subprocess.run(
            ["ping", param, "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

print("Waiting for computer to connect...")
print()

while True:
    ip = get_ip(HOSTNAME)

    if ip and is_reachable(ip):
        print(f"Computer is online!")
        print(f"Hostname : {HOSTNAME}")
        print(f"IP       : {ip}")
        break

    time.sleep(2)
