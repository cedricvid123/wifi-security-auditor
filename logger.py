import json
from datetime import datetime

def parse_and_log(output, bssid, report_file='reports/report.json'):
    timestamp = datetime.now().isoformat()
    if "KEY FOUND!" in output:
        key_line = [line for line in output.splitlines() if "KEY FOUND!" in line][0]
        key = key_line.split('[')[-1].strip(']')
        result = {"bssid": bssid, "key": key, "status": "success", "time": timestamp}
    else:
        result = {"bssid": bssid, "key": None, "status": "failed", "time": timestamp}
    
    with open(report_file, 'w') as f:
        json.dump(result, f, indent=4)
    
    print(f"[*] Result saved to {report_file}")
    return result
