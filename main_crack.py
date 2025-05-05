from capture.capture import capture_handshake
from crack.crack import crack_password
from utils.logger import parse_and_log

iface = "wlan0mon"
bssid = "AA:BB:CC:DD:EE:FF"
channel = "6"
cap_prefix = "target_capture"
wordlist = "/usr/share/wordlists/rockyou.txt"

# Step 1: Capture
capture_handshake(iface, bssid, channel, cap_prefix)

# Step 2: Crack
output = crack_password(f"captures/{cap_prefix}-01.cap", wordlist, bssid)

# Step 3: Log result
parse_and_log(output, bssid)
