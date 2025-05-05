import subprocess

def crack_password(cap_file, wordlist, bssid):
    print(f"[*] Cracking password using {wordlist}...")
    result = subprocess.run(['aircrack-ng', '-w', wordlist, '-b', bssid, cap_file],
                            capture_output=True, text=True)
    return result.stdout
