# Entry point of the tool

from scanner.wifi_scanner import scan_networks
from scanner.rogue_detector import load_known_aps, detect_rogue_aps
from scanner.rogue_detector import detect_duplicate_ssids
from scanner.rogue_detector import update_signal_history, detect_signal_fluctuation


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
    
    rogues = detect_duplicate_ssids(networks)
    
    print("\n--- Possible Rogue Access Points ---")
    for ap in rogues:
        print(f"[!] SSID: {ap['ssid']}, BSSIDs: {', '.join(ap['bssids'])}")
        
    # After scan:
    update_signal_history(networks)

    # After a few iterations or with delay:
    fluctuating = detect_signal_fluctuation()

    print("\n--- Unstable Signal BSSIDs ---")
    for ap in fluctuating:
        print(f"[!] BSSID: {ap['bssid']} — Fluctuation: {ap['fluctuation']} dBm")
