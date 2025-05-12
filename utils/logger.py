import csv
import json
from datetime import datetime
import os

# === Ensure 'data' directory exists ===
data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# === CSV Logger ===
def log_results_to_csv(networks, filename="data/wifi_scan_results.csv"):
    """
    Logs the scan results to a CSV file. Creates the file if it doesn't exist.

    Parameters:
    ----------
    networks : list of dict
        A list of dictionaries containing WiFi network information.
    filename : str, optional
        The name of the CSV file to log results into (default is "data/wifi_scan_results.csv").
    """
    header = ["Timestamp", "SSID (Name)", "BSSID (MAC Address)", "Signal Strength (dBm)", "Encryption Type"]

    with open(filename, mode='a+', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        file.seek(0)
        first_char = file.read(1)

        if not first_char:
            writer.writerow(header)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for network in networks:
            writer.writerow([
                timestamp,
                network["SSID"],
                network["BSSID"],
                network["Signal"],
                network["Encryption"]
            ])

    print(f"\n✅ Results successfully logged to {filename}")


# === JSON Logger ===
def log_results_to_json(networks, filename="data/wifi_scan_results.json"):
    """
    Logs the scan results to a JSON file. Overwrites the file with the latest scan.

    Parameters:
    ----------
    networks : list of dict
        A list of dictionaries containing WiFi network information.
    filename : str, optional
        The name of the JSON file to log results into (default is "data/wifi_scan_results.json").
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    json_data = {
        "timestamp": timestamp,
        "networks": networks
    }

    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4)

    print(f"\n✅ Results successfully logged to {filename}")
