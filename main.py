import os
import time
from wifi_scanner import scan_wifi_networks
from result_logger import log_results_to_csv, log_results_to_json

# === Global Variables ===
CSV_FILE = "data/wifi_scan_results.csv"
JSON_FILE = "data/wifi_scan_results.json"

# === Ensure 'data' directory exists ===
if not os.path.exists('data'):
    os.makedirs('data')


# === Main Workflow Controller ===
def main():
    print("🚀 Starting WiFi Security Auditor...")
    print("===================================")

    while True:
        print("\nChoose an option:")
        print("[1] Scan for WiFi networks")
        print("[2] View last scan results")
        print("[3] Export to CSV and JSON")
        print("[4] Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            print("\n🔍 Scanning for networks...")
            networks = scan_wifi_networks()
            print("\n✅ Scan complete.")
            log_results_to_csv(networks, CSV_FILE)
            log_results_to_json(networks, JSON_FILE)

        elif choice == '2':
            if os.path.exists(CSV_FILE):
                print("\n📂 Displaying last scan results:")
                with open(CSV_FILE, 'r') as file:
                    print(file.read())
            else:
                print("\n❌ No results found. Please scan first.")

        elif choice == '3':
            if os.path.exists(CSV_FILE) and os.path.exists(JSON_FILE):
                print(f"\n✅ Data successfully exported to:\n- {CSV_FILE}\n- {JSON_FILE}")
            else:
                print("\n❌ No data to export. Please scan first.")

        elif choice == '4':
            print("\n👋 Exiting WiFi Security Auditor. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")

        print("\n===============================")
        time.sleep(2)  # Wait before refreshing options


# === Main Script Entry Point ===
if __name__ == "__main__":
    main()
