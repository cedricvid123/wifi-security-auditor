from capture.capture import capture_handshake
from crack.crack import crack_password
from utils.logger import parse_and_log
import os

def capture_and_crack():
    # === USER CONFIG ===
    interface = "wlan0mon"  # must be in monitor mode
    bssid = input("Enter target BSSID: ")
    channel = input("Enter channel: ")
    wordlist = input("Enter path to wordlist: ")  # e.g., /usr/share/wordlists/rockyou.txt
    cap_prefix = input("Enter filename prefix for capture: ")  # e.g., target_ap
    
    cap_file_path = f"captures/{cap_prefix}-01.cap"

    # === STEP 1: CAPTURE ===
    if not os.path.exists(cap_file_path):
        capture_handshake(interface, bssid, channel, cap_prefix)
    else:
        print(f"[!] Capture file {cap_file_path} already exists. Skipping capture...")

    # === STEP 2: CRACK ===
    output = crack_password(cap_file_path, wordlist, bssid)

    # === STEP 3: LOG ===
    parse_and_log(output, bssid)

if __name__ == "__main__":
    capture_and_crack()
