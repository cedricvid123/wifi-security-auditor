# Entry point of the tool

from scanner.wifi_scanner import scan_networks
from scanner.rogue_detector import load_known_aps, detect_rogue_aps

if __name__ == "__main__":
    networks = scan_networks()
    known_aps = load_known_aps()
    rogue_aps = detect_rogue_aps(networks, known_aps)

    print("\n--- All Detected Networks ---")
    for net in networks:
        print(f"{net['ssid']:20} {net['bssid']:20} Signal: {net['signal']}")

    print("\n--- Suspected Rogue APs ---")
    for rogue in rogue_aps:
        print(f"[!] {rogue['ssid']} ({rogue['bssid']}) — Possible Evil Twin")
