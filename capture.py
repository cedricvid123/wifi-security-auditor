import subprocess
import os

def capture_handshake(interface, bssid, channel, output_prefix):
    os.makedirs('captures', exist_ok=True)
    print("[*] Starting handshake capture...")
    cap_path = f'captures/{output_prefix}'
    subprocess.run(['airodump-ng', '--bssid', bssid, '-c', channel, '-w', cap_path, interface])
    print("[*] Capture complete.")
