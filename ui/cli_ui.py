# CLI interface placeholder
import time
from scanner.wifi_scanner import scan_networks
from scanner.rogue_detector import (
    detect_duplicate_ssids,
    update_signal_history,
    detect_signal_fluctuation
)

def show_menu():
    print("\n=== Wi-Fi Security Auditing Tool ===")
    print("1. Scan for Wi-Fi networks")
    print("2. Detect Rogue Access Points (Evil Twins)")
    print("3. Detect Signal Fluctuations")
    print("4. Exit")

def run_cli():
    while True:
        show_menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
            networks = scan_networks()
            print("\n--- Detected Wi-Fi Networks ---")
            for net in networks:
                print(f"{net['ssid']:20} {net['bssid']:20} Ch:{net['channel']}  Signal:{net['signal']}  Encrypt:{net['encryption']}")
            update_signal_history(networks)

        elif choice == "2":
            networks = scan_networks()
            rogues = detect_duplicate_ssids(networks)
            print("\n--- Possible Rogue APs ---")
            if rogues:
                for ap in rogues:
                    print(f"[!] SSID: {ap['ssid']} — BSSIDs: {', '.join(ap['bssids'])}")
            else:
                print("No rogue APs detected.")

        elif choice == "3":
            results = detect_signal_fluctuation()
            print("\n--- Unstable Signal APs ---")
            if results:
                for ap in results:
                    print(f"[!] BSSID: {ap['bssid']} — Fluctuation: {ap['fluctuation']} dBm")
            else:
                print("No suspicious signal behavior detected.")

        elif choice == "4":
            print("Exiting.")
            break

        else:
            print("Invalid option. Please try again.")

        time.sleep(1)
