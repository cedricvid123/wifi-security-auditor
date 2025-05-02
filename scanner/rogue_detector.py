# Rogue AP detection logic

import json

def load_known_aps(file_path='config/known_aps.json'):
    with open(file_path, 'r') as file:
        return json.load(file)

def detect_rogue_aps(scanned_aps, known_aps):
    rogue_aps = []

    known_pairs = {(ap['ssid'], ap['bssid']) for ap in known_aps}

    for ap in scanned_aps:
        ssid_bssid = (ap['ssid'], ap['bssid'])

        if ap['ssid'] == "":
            continue  # Skip hidden SSIDs

        if ssid_bssid not in known_pairs:
            # Could be rogue if SSID is known but BSSID is not
            if any(ap['ssid'] == k['ssid'] for k in known_aps):
                ap['suspected'] = True
                rogue_aps.append(ap)

    return rogue_aps
