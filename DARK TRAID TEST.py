#!/usr/bin/env python3
"""
DARK-TRAID Menu Launcher with Red Map Geolocation (Dark Red ASCII)
"""

import os
import sys
import time
import webbrowser
import socket

try:
    import requests
except ImportError:
    print("Installing requests module...")
    os.system(f"{sys.executable} -m pip install requests")
    import requests

# ====== STARTUP ASCII LOGO ======
LOGO = r"""
                                              .*.                                             
                                             .%@@.                                            
                                            .%@@@@.                                           
                                           .@@@%@@@.                                          
                                          .@@@+ =@@@:                                         
                                         :@@@=   -@@@-                                        
                                        :@@@-     :@@@-                                       
                                       -@@@-       .@@@=   ..+.                               
                               .+:.   =@@@:         .@@@+.%%-.*.                              
                               .:%*%-+@@@.           .@@@* .:=++.                             
                              *@%%@-+@@@.             .%@@#.@.%:*.                            
                            .##.:%:*@@@.               .%@@%:%%.=*                            
                           .=%%:*:#@@%.                 .%@@%.:*@%%.                          
                           :%#:*.%@@%.                   .#@@@...+@%.                         
                         :#-*#:.@@@#.                     .*@@@.#: :%                         
                         .%+.#:@@@#.                       .*@@@.+#.*@.                       
                       :+:%%:.@@@*.                         .+@@@:+-+=+:                      
                     .:.+::%:@@@*  +@@@@@@@:@#   *@:.@@@@@@#  =@@@:+@-+#:.                   
                     .+:*%-:@@@+     .%@.  :@#...*@:.@@.       -@@@-:%  *-                   
                    -*  @::@@@=      .%@.  :@@%%%@@:.@@@@@%:    -@@@==@%=-+.                 
                   ..*%##-@@@=       .%@.  :@#   *@:.@@.         :@@@=:@#-=+                 
                  *=-@@.=@@@-        .%@.  :@#   *@:.%@@@@@%      :@@@+...---.               
                 .:%@. +@@@: ......      ....   .......  ...   ... .@@@*.:*#==               
                *@%@*.+@@@:  =@@#%@@%.  .%@@=  .@@###@@#.=@% :@@+.  .@@@*.#.:%%.             
               : -@- *@@@.   =@#   =@#  +@=%@: .@@.  :@%.=@%%@+.     .@@@#.+...%.            
             ...+@+:#@@@.    =@#   -@% :@@.:@%..@@@@@@%: =@@#@@=       %@@#.*#%...           
            ..%%:..#@@@.     =@#  .@@=.@@%%%@@*.@@.  :@% =@% .%@*      .%@@%..%@:+:          
                ..%@@%       -%%%%%+. +%+   .#%-%%.  .%%.=%#   *%#.      *@@%.  *#-:         
                .%@@#   ....................  ....    .....    .........  *@@@.=.             
               .%@@*.   %@@@@@@@@@.%@@@@@@@@*..%@%    +@@@*    #@@@@@@@@+. +@@@.              
              .@@@*        -@@=    %@#    *@@:.%@%   .@@*@@:   #@@.   -@@+  =@@@:             
             .@@@+         -@@=    %@@***#@@=..%@%   %@*.*@@   #@@.    @@%.  -@@@:            
            :@@@=          -@@=    %@@***%@@=..%@%  *@@===@@#. #@@.    @@#.   :@@@-           
           -@@@-           -@@=    %@#   .#@@..%@% :@@*****@@: #@@. .:@@@-     :@@@=          
          -@@@:            -@@=    %@#    =@@:.%@%.@@#.   .#@@.#@@@@@@@#.       .@@@+         
         =@@@..                                                                  .@@@*        
        +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#       
       *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#      
                :@=.@#.+@..##%-*- %:%.:@-+= %=@##:%  *= .%..@=.#+.%:%:%*#:@=.@#               
                :#%++#.@-*=*  .*%#@:@.%:@.@++-@#*:%  *= .%.#:@:%=#%:@.+@@-#%++#               
                .+:+:+*. *:=#*.+: *:*== :+-#.:###:###+##+*:* .**.:*.*.##+:+:+:+               
"""

# ====== RED MAP ASCII LOGO ======
RED_MAP_LOGO = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡇⠀⠀⢀⣼⠗⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# ====== SIMPLE ASCII WORLD MAP ======
SIMPLE_MAP = [
"                         _.-'''-._                         ",
"                    _.-'           '-._                    ",
"                 .-'                   '-.                 ",
"               .'                         '.               ",
"             .'                             '.             ",
"            /        .-~~~~-..-~~~~-.          \\           ",
"           /      .-~  .-~  :  .-~  ~-.         \\         ",
"          ;     /      :     :     :    \\        ;        ",
"         |     ;       :     :     :     ;       |        ",
"         |     |       :     :     :     |       |        ",
"         |     |       :     :     :     |       |        ",
"         ;     ;       :     :     :     ;       ;        ",
"          \\     \\      :     :     :    /       /         ",
"           \\     '.     '-. .-._.-'   .'      /          ",
"            '.     '-._         _.-'     _.-'           ",
"              '.        ''-----''       .'             ",
"                '-._             _.-'                 ",
"                    '-._     _.-'                     ",
"                         ''''                          ",
]

MAP_WIDTH = len(SIMPLE_MAP[0])
MAP_HEIGHT = len(SIMPLE_MAP)

# ====== UTILS ======
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(seconds=0.8):
    time.sleep(seconds)

def fade_in_logo_two_tone(logo_text, delay=0.004):
    border_chars = set("*@#+-=:")
    for line in logo_text.splitlines():
        colored_line = ""
        for char in line:
            if char in border_chars:
                colored_line += "\033[31m" + char  # dark red
            elif char.strip():
                colored_line += "\033[90m" + char  # dark gray
            else:
                colored_line += char
        print(colored_line + "\033[0m")
        time.sleep(delay)

# ====== RED MAP FUNCTIONS ======
def fetch_ip_info(query_ip_or_host):
    try:
        resolved_ip = socket.gethostbyname(query_ip_or_host)
    except Exception:
        resolved_ip = query_ip_or_host
    api_url = f"http://ip-api.com/json/{resolved_ip}?fields=status,message,country,regionName,city,zip,lat,lon,isp,org,query"
    try:
        r = requests.get(api_url, timeout=8)
        return r.json()
    except Exception as e:
        return {"status": "fail", "message": str(e)}

def plot_on_map(lat, lon):
    x = int((lon + 180.0) / 360.0 * MAP_WIDTH)
    y = int((90.0 - lat) / 180.0 * MAP_HEIGHT)
    x = max(0, min(MAP_WIDTH - 1, x))
    y = max(0, min(MAP_HEIGHT - 1, y))
    out_lines = []
    for row_idx, line in enumerate(SIMPLE_MAP):
        row_chars = list(line.ljust(MAP_WIDTH))
        if row_idx == y:
            row_chars[x] = "\033[91mX\033[0m"
        colored = ""
        for ch in row_chars:
            if ch.startswith("\033[91m"):
                colored += ch
            else:
                if ch.strip():
                    colored += "\033[31m" + ch + "\033[0m"  # dark red
                else:
                    colored += ch
        out_lines.append(colored)
    return out_lines

def red_map():
    clear()
    print("\033[31m========== THE RED MAP ==========\033[0m\n")
    
    # Print RED_MAP_LOGO in dark red
    for line in RED_MAP_LOGO.splitlines():
        colored_line = ""
        for char in line:
            if char.strip():
                colored_line += "\033[31m" + char + "\033[0m"
            else:
                colored_line += char
        print(colored_line)
    
    print("\nEnter an IP address or hostname to geolocate (empty to cancel).")
    query = input("\nIP / Hostname: ").strip()
    if not query:
        return

    print("\nResolving and querying geolocation provider...")
    data = fetch_ip_info(query)
    time.sleep(0.3)

    if data.get("status") != "success":
        print(f"\n\033[91mLookup failed:\033[0m {data.get('message','unknown error')}")
        input("\nPress Enter to return to menu...")
        return

    country = data.get("country", "")
    region = data.get("regionName", "")
    city = data.get("city", "")
    zipc = data.get("zip", "")
    lat = float(data.get("lat", 0.0))
    lon = float(data.get("lon", 0.0))
    isp = data.get("isp", "")
    org = data.get("org", "")
    query_ip = data.get("query", "")

    print("\n\033[92mGeolocation result:\033[0m")
    print(f"  IP:     {query_ip}")
    print(f"  Country:{country}")
    print(f"  Region: {region}")
    print(f"  City:   {city} {zipc}")
    print(f"  Lat/Lon:{lat}, {lon}")
    print(f"  ISP:    {isp}")
    print(f"  Org:    {org}")

    print("\nApproximate location on map (X):\n")
    plotted = plot_on_map(lat, lon)
    for pl in plotted:
        print(pl)
    input("\nPress Enter to return to menu...")

# ====== OTHER ACTIONS ======
def open_github_tool():
    url = "https://github.com/GR1M-swat/snipe"
    print(f"\nOpening DARK-name-swat-tool GitHub page:\n{url}\n")
    pause(1)
    webbrowser.open(url)
    input("Press Enter to return to menu...")

def about():
    clear()
    print("\033[94m========== ABOUT DARK-TRAID ==========\033[0m\n")
    print("DARK-TRAID launcher with animated ASCII art and The Red Map geolocator.")
    print("Use The Red Map responsibly: education/testing only.\n")
    print("=== CREDITS ===")
    print("Team: ENDERPRIZE")
    print("Contributors:")
    print(" - mikender (you)")
    print(" - 33011free-the-internet (friend, helped with naming)\n")
    print("GitHub Repository: https://github.com/GR1M-swat/snipe")
    input("\nPress Enter to return to menu...")

def quit_program():
    print("\nGoodbye!")
    pause(0.5)
    sys.exit(0)

# ====== MENU ======
MENU_OPTIONS = {
    "1": ("Open DARK-name-swat-tool GitHub page", open_github_tool),
    "2": ("The Red Map (IP geolocate)", red_map),
    "3": ("About / Credits", about),
    "0": ("Quit", quit_program),
}

def show_menu():
    clear()
    print("\033[91m========== DARK-TRAID ==========\033[0m\n")
    for key, (label, _) in MENU_OPTIONS.items():
        print(f"  [{key}] {label}")
    print()

def main():
    try:
        clear()
        fade_in_logo_two_tone(LOGO, delay=0.0035)
        time.sleep(1.0)
        clear()
        while True:
            show_menu()
            choice = input("Enter choice: ").strip()
            action = MENU_OPTIONS.get(choice)
            if action:
                clear()
                print(f"-> {action[0]}\n")
                action[1]()
            else:
                print("\033[91mInvalid choice.\033[0m")
                time.sleep(0.6)
    except KeyboardInterrupt:
        quit_program()

if __name__ == "__main__":
    main()
