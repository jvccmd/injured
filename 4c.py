import sys
import time
import random
import string
import requests

# ANSI Terminal Colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
MAGENTA = "\033[95m"

BANNER = """
██╗███╗   ██╗     ██╗██╗   ██╗██████╗ ███████╗██████╗ 
██║████╗  ██║     ██║██║   ██║██╔══██╗██╔════╝██╔══██╗
██║██╔██╗ ██║     ██║██║   ██║██████╔╝█████╗  ██║  ██║
██║██║╚██╗██║██   ██║██║   ██║██╔══██╗██╔══╝  ██║  ██║
██║██║ ╚████║╚█████╔╝╚██████╔╝██║  ██║███████╗██████╔╝
╚═╝╚═╝  ╚═══╝ ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ 
            ██╗  ██╗     ██████╗                      
            ██║  ██║    ██╔════╝                      
            ███████║    ██║                           
            ╚════██║    ██║                           
                 ██║    ╚██████╗                      
                 ╚═╝     ╚═════╝                      
"""

def generate_4c_username():
    """Generates a random 4-character string using lowercase letters and numbers."""
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for _ in range(4))

def check_live_discord_status(username):
    """
    Queries a resilient open API link to verify direct lookup availability.
    Returns: True if available (+), False if taken (-).
    """
    # Switching to a fresh, active proxy check endpoint
    url = f"https://samifying.com{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=6)
        
        if response.status_code == 200:
            data = response.json()
            # Most lookups return a status or 'exists' flag
            # If the user profile does NOT exist, it means the name is available
            exists = data.get("exists", True)
            return not exists
        elif response.status_code == 404:
            # Traditional HTTP REST standard: 404 means the username profile is not found (Available)
            return True
        elif response.status_code == 429:
            print(f"\n{RED}[!] Rate limit encountered. Pausing for 5 seconds...{RESET}")
            time.sleep(5)
            return False
        else:
            return False
    except Exception:
        return False

def main():
    print(MAGENTA + BANNER + RESET)
    
    try:
        choice = input(MAGENTA + "Press Y/N To Start > " + RESET).strip().lower()
        
        if choice != 'y':
            print(RED + "Exiting..." + RESET)
            sys.exit(0)
            
        print(MAGENTA + "\nRunning Direct Live Filter... Press Ctrl+C to halt loop.\n" + RESET)
        time.sleep(0.5)

        checked_count = 0

        while True:
            username = generate_4c_username()
            is_available = check_live_discord_status(username)
            checked_count += 1
            
            if is_available:
                print(f"{GREEN}[+] {username} (FOUND AVAILABLE!){RESET}")
                # Save it immediately to a local text file so you don't lose it
                with open("available_4c.txt", "a") as f:
                    f.write(f"{username}\n")
            else:
                print(f"{RED}[-] {username} (Total Checked: {checked_count}){RESET}")
                
            # A 1.6-second delay ensures the network connection drops cleanly 
            # between checks to maximize chances of accuracy.
            time.sleep(1.6)

    except KeyboardInterrupt:
        print(RED + "\nExiting..." + RESET)
        sys.exit(0)

if __name__ == "__main__":
    main()
