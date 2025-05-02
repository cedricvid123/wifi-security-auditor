# Entry point of the tool

from scanner.wifi_scanner import scan_networks

if __name__ == "__main__":
    networks = scan_networks()
    for net in networks:
        print(f"SSID: {net['ssid']}, BSSID: {net['bssid']}, Channel: {net['channel']}, Encryption: {net['encryption']}, Signal: {net['signal']}")
