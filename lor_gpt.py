import socket
import subprocess
import sys
from datetime import  datetime

# Lor GPT - Penetration Testing Tool


def print_banner():
    banner = """
    ====================================
           Lori GPT v1.0
      Penetration Testing Suite
    ====================================
    """
    print(banner)

def scan_ports(target, start_port=1, end_port=1000):
    open_ports = []
    print(f"\n[*] Scanning {target} for open ports...")
    for port in range(start_port, end_port +1):
        try:
           sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           sock.settimeout(0.5)
           result = sock.connect_ex((target, port))
           if result == 0:
               open_ports.append(port)
               print(f"[*] Port {port} is OPEN")
           sock.close()
        except:
           pass
    return open_ports
def main():
    print_banner()
    target = input("\n[*] Enter target IP or hostname: ")
    try:
       print(f"\n[*] Target: {target}")
       print(f"\n[*] Start time: {datetime.now()}")
       open_ports = scan_ports(target)
       if open_ports:
          print(f"\n[+] Found {len(open_ports)} open ports: {open_ports}")
       else:
           print("\n[-] No open_ports found")
       print(f"[*] End time{datetime.now()}")
    except Exception as e:
       print(f"[-] Error: {e}")
if __name__ == "__main__":
    main()
       
