# Wi-Fi-security-auditor
Wi-Fi security auditing is the process of analyzing, testing, and assessing the security posture of a wireless network to identify vulnerabilities, misconfigurations, and potential weaknesses that could be exploited by attackers.

# 1. Import Required Libraries

Explanation:

· pywifi: This library is used to interact with the WiFi interface.

· const: Contains constants for interface status and encryption.

· time: Allows for delays (useful while scanning for networks).

· prettytable: For displaying networks in a structured table format.

---

# 2. Initialize the WiFi Interface


CopyEdit
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

Explanation:

· pywifi.PyWiFi(): Initializes the WiFi manager.

· wifi.interfaces()[0]: Gets the first wireless interface. If you have multiple adapters, you may need to select a different index.

---

# 3. Start Scanning for Networks

python
CopyEdit
iface.scan()
print("Scanning for WiFi networks...")
time.sleep(3) # Wait for scan results to populate

Explanation:

· iface.scan(): Sends a scan request to the WiFi adapter.

· time.sleep(3): Allows the scan to complete and gather information. This delay is necessary because the scan runs asynchronously.

---

# 4. Fetch the Scan Results

python
CopyEdit
scan_results = iface.scan_results()

Explanation:

· iface.scan_results(): Retrieves a list of all networks found during the scan.

· Each network in this list is an object containing attributes like ssid, bssid, signal, and akm.

---

# 5. Create a Pretty Table for Display

python
CopyEdit

table = PrettyTable(["SSID (Name)", "BSSID (MAC Address)", "Signal Strength (dBm)", "Encryption Type"])
networks = []

Explanation:

· PrettyTable: This library is used to format the data into a clean, readable table.

· networks: A list to store all the scanned WiFi network details.

---

# 6. Loop Through Networks and Collect Data

python
CopyEdit
for network in scan_results:
     ssid = network.ssid
     bssid = network.bssid
     signal = network.signal
     
     # Determine encryption type
     if network.akm:
         encryption = " / ".join([str(akm).split('.')[-1] for akm in network.akm])
         else:
         encryption = "Open"
         
         # Append data to the list
         networks.append({"SSID": ssid,"BSSID": bssid,"Signal": signal,"Encryption": encryption})
         
         # Add to the display table
         table.add_row([ssid, bssid, signal, encryption]))

Explanation:

· Loops through all the networks found.

· Extracts:
    o SSID → Network name.
    o BSSID → MAC address.
    o Signal → Signal strength in dBm.
    o Encryption → Security type (WPA, WPA2, Open, etc.).

· Appends the data to:
    o A list (networks) for easy access.
    o A formatted table (table) for pretty display.

---

# 7. Display the Networks

python
CopyEdit
  print(table)

Explanation:

· This prints out the complete list of WiFi networks in a clean, readable format.

---

# 8. Return the List of Networks

python
CopyEdit
  return networks

Explanation:

· The list of networks is returned for further processing if needed.

---

# 9. Main Function Entry Point

python
CopyEdit
if __name__ == "__main__":
    networks = scan_wifi_networks()

Explanation:

· This ensures the script runs only if it is executed directly (not imported).

· Calls the main function to execute the scan.

---

Full Script: wifi_scanner.py

python
CopyEdit
import pywifi
from pywifi import const
import time
from prettytable import PrettyTable

def scan_wifi_networks():
   # Initialize the WiFi interface
   wifi = pywifi.PyWiFi()
   
   iface = wifi.interfaces()[0]
   
   # Start scanning
   iface.scan()
   
   print("Scanning for WiFi networks...")
   
   time.sleep(3) # Wait for scan results
   
   # Get scan results
   scan_results = iface.scan_results()
   
   # Create a formatted table for display
   table = PrettyTable(["SSID (Name)", "BSSID (MAC Address)", "Signal Strength (dBm)", "Encryption Type"])
   networks = []
   
   for network in scan_results:
   ssid = network.ssid
   bssid = network.bssid
   signal = network.signal
   
   # Determine encryption type
   if network.akm:
   encryption = " / ".join([str(akm).split('.')[-1] for akm in network.akm])
   else:
      encryption = "Open"
    
    # Append data to the list
    networks.append({"SSID": ssid, "BSSID": bssid, "Signal": signal, "Encryption": encryption})
    
    # Add to the display table
    table.add_row([ssid, bssid, signal, encryption])
    
    # Display the networks in table format
    print(table)
    
    # Return the list of networks
    return networks

if __name__ == "__main__":
   networks = scan_wifi_networks()

---

# To Run the Script

bash
CopyEdit
python wifi_scanner.py

---

Repository Structure

|-- capture/                # Handles packet capturing functionalities
|-- config/                 # Configuration files and settings
|-- crack/                  # Password cracking mechanisms
|-- reports/                # Generated audit reports
|-- scanner/                # Wi-Fi network scanning
|-- ui/                     # User interface components
|-- utils/                  # Utility functions
|-- main.py                 # Main entry point for the application
|-- main_crack.py           # Password cracking process
|-- crack_and_capture.py    # Integrated scanning, capturing, and cracking
|-- requirements.txt        # List of dependencies
|-- README.md               # Project documentation
|-- LICENSE                 # License information

---
# Installation

1. Clone the repository
git clone https://github.com/cedricvid123/wifi-security-auditor.git

cd wifi-security-auditor

3. Install dependencies:

   pip install -r requirements.txt

4. Ensure system tools are available (e.g., aircrack-ng):

   sudo apt-get install aircrack-ng

---

# Usage

To scan available Wi-Fi networks:

python main.py

Cracking Passwords

To initiate password cracking:

python main_crack.py

Combined Capture and Crack

To perform packet capturing and password cracking:

python crack_and_capture.py

---
