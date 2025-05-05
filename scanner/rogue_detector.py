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

    def detect_duplicate_ssids(networks):
    ssid_map = {}

    for net in networks:
        ssid = net['ssid']
        bssid = net['bssid']

        if ssid not in ssid_map:
            ssid_map[ssid] = set()
        ssid_map[ssid].add(bssid)

    # Flag SSIDs with multiple BSSIDs
    rogue_aps = []
    for ssid, bssids in ssid_map.items():
        if len(bssids) > 1:
            rogue_aps.append({
                "ssid": ssid,
                "bssids": list(bssids),
                "reason": "Multiple BSSIDs detected (possible Evil Twin)"
            })

    return rogue_aps
