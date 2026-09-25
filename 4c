import sys
import time
import random
import string
import requests  # This module sends the real live web requests

# ANSI Terminal Colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
MAGENTA = "\033[95m"

# Thick retro block font layout matching your reference image
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
    Queries an open-source Discord lookup gateway API to verify actual availability.
    Returns True if available (+), False if taken (-).
    """
    url = f"https://api.lixqa.de/v3/discord/pomelo/{username}"
    try:
        # Send a live request to the endpoint tracking system
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            # If 'available' is true inside the JSON response data data package
            return data.get("available", False)
        else:
            # Fallback if server is busy or rate limiting your connection
            return False
    except Exception:
        # If network error or timeout occurs, safely mark as unavailable to prevent false positives
        return False

def main():
    # Print the block header banner in magenta
    print(MAGENTA + BANNER + RESET)
    
    try:
        # Get user permission before initiating tracking loops
        choice = input(MAGENTA + "Press Y/N To Start > " + RESET).strip().lower()
        
        if choice != 'y':
            print(RED + "Exiting..." + RESET)
            sys.exit(0)
            
        print(MAGENTA + "\nRunning Real Live Checks... Press Ctrl+C to halt loop.\n" + RESET)
        time.sleep(0.5)

        while True:
            username = generate_4c_username()
            
            # Grabs true validation data from the server API instead of fake math percentages
            is_available = check_live_discord_status(username)
            
            if is_available:
                print(f"{GREEN}[+] {username}{RESET}")
            else:
                print(f"{RED}[-] {username}{RESET}")
                
            # Crucial: Live lookups need a 2-second gap so Discord APIs don't block your connection
            time.sleep(2.0)

    except KeyboardInterrupt:
        # Catches Ctrl+C cleanly and displays the custom exit string in red
        print(RED + "\nExiting..." + RESET)
        sys.exit(0)

if __name__ == "__main__":
    main()
