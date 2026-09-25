import sys
import time
import random
import string

# ANSI Terminal Colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
MAGENTA = "\033[95m"

# Thick retro block font layout
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

def main():
    print(MAGENTA + BANNER + RESET)
    
    try:
        # Match user request input string explicitly
        choice = input(MAGENTA + "Press Y/N To Start > " + RESET).strip().lower()
        
        if choice != 'y':
            print(RED + "Exiting..." + RESET)
            sys.exit(0)
            
        print(MAGENTA + "\nRunning Local Simulator... Press Ctrl+C to halt loop.\n" + RESET)
        time.sleep(0.5)

        checked_count = 0

        while True:
            username = generate_4c_username()
            checked_count += 1
            
            # Adjusted percentage rate to ensure green hits [+] drop frequently on your screen
            is_available = random.random() < 0.08
            
            if is_available:
                print(f"{GREEN}[+] {username} (Total Checked: {checked_count}){RESET}")
                # Save it immediately to a local text file
                with open("available_4c.txt", "a") as f:
                    f.write(f"{username}\n")
            else:
                print(f"{RED}[-] {username} (Total Checked: {checked_count}){RESET}")
                
            # Balanced delay for terminal scroll comfort
            time.sleep(0.2)

    except KeyboardInterrupt:
        # Handles user aborting the loop via Ctrl+C
        print(RED + "\nExiting..." + RESET)
        sys.exit(0)

if __name__ == "__main__":
    main()
