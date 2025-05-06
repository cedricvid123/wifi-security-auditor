import subprocess
import os
import time
import signal

def capture_handshake(interface, bssid, channel, output_prefix):
    os.makedirs('captures', exist_ok=True)
    print("[*] Starting handshake capture...")

    cap_path = f'captures/{output_prefix}'
    csv_path = f'{cap_path}-01.csv'

    # Launch airodump-ng in the background
    airodump = subprocess.Popen([
        'airodump-ng',
        '--bssid', bssid,
        '-c', channel,
        '--write-interval', '1',
        '-w', cap_path,
        interface
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        print("[*] Waiting for WPA handshake...")
        while True:
            time.sleep(3)
            if os.path.exists(csv_path):
                with open(csv_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if "WPA handshake" in content:
                        print("[+] WPA handshake captured!")
                        break
    finally:
        os.kill(airodump.pid, signal.SIGTERM)
        print("[*] Capture stopped.")
