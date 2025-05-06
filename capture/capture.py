import subprocess
import time
import os
import signal

def capture_handshake(interface, bssid, channel, output_prefix):
    print("[*] Starting handshake capture...")

    capture_file = f"captures/{output_prefix}"
    airodump = subprocess.Popen([
        'airodump-ng',
        '-c', channel,
        '--bssid', bssid,
        '-w', capture_file,
        interface
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Monitor for handshake indicator in the .csv companion file
    csv_file = f"{capture_file}-01.csv"
    
    try:
        while True:
            time.sleep(3)
            if os.path.exists(csv_file):
                with open(csv_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if "WPA handshake" in content:
                        print("[+] WPA handshake captured!")
                        break
    finally:
        os.kill(airodump.pid, signal.SIGTERM)
        print("[*] Capture complete.")
