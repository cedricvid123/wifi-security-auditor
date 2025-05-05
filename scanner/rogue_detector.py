# Rogue AP detection logic

import json
import time

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

    rogue_aps = []
    for ssid, bssids in ssid_map.items():
        if len(bssids) > 1:
            rogue_aps.append({
                "ssid": ssid,
                "bssids": list(bssids),
                "reason": "Multiple BSSIDs detected (possible Evil Twin)"
            })

    return rogue_aps

signal_history = {}

def update_signal_history(networks, time_window=60):
    current_time = time.time()

    for net in networks:
        bssid = net['bssid']
        rssi = net['signal']

        if bssid not in signal_history:
            signal_history[bssid] = []

        signal_history[bssid].append((current_time, rssi))

        # Clean old entries
        signal_history[bssid] = [
            (t, s) for t, s in signal_history[bssid]
            if current_time - t <= time_window
        ]

def detect_signal_fluctuation(threshold=20):
    suspicious = []
    for bssid, history in signal_history.items():
        rssi_values = [s for t, s in history]
        if len(rssi_values) >= 2:
            fluctuation = max(rssi_values) - min(rssi_values)
            if fluctuation > threshold:
                suspicious.append({
                    "bssid": bssid,
                    "fluctuation": fluctuation,
                    "reason": "Signal fluctuation over time (possible rogue or mobile AP)"
                })
    return suspicious
