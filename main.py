# Entry point of the tool

from ui.cli_ui import run_cli


if __name__ == "__main__":
    run_cli()
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
