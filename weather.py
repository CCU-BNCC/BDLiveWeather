#!/usr/bin/env python3
# BDLiveWeather - Made in MD Abdullah 🇧🇩

import os
import time
import requests
from datetime import datetime
from colorama import Fore, Style, init
import curses

init(autoreset=True)

# ===== Load Banner =====
def load_banner():
    if os.path.exists("banner.txt"):
        with open("banner.txt", "r") as b:
            print(b.read())
    else:
        print("=== BDLiveWeather ===")

# ===== Load Districts (return as list) =====
def load_districts():
    if os.path.exists("districts.txt"):
        with open("districts.txt", "r") as d:
            return [line.strip() for line in d if line.strip()]
    else:
        print("District list not found!")
        return []

# ===== GUI Arrow-Key Menu =====
def select_district(districts):
    def menu(stdscr):
        curses.curs_set(0)
        current_row = 0
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Select Your District using ↑ ↓ and Enter:\n", curses.A_BOLD)
            for i, district in enumerate(districts):
                if i == current_row:
                    stdscr.addstr(i+2, 2, f"> {district}", curses.color_pair(1))
                else:
                    stdscr.addstr(i+2, 2, f"  {district}")
            key = stdscr.getch()
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(districts) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return districts[current_row]
    curses.wrapper(lambda stdscr: curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN))
    return curses.wrapper(lambda stdscr: menu(stdscr))

# ===== Live Weather =====
def get_weather(city):
    try:
        print(Fore.YELLOW + "\n[🔴 Live Weather]".center(40, "-"))
        url = f"https://wttr.in/{city}?format=%l:+%c+%t+%h+%w\n"
        res = requests.get(url)
        if res.status_code == 200:
            print(res.text)
        else:
            print(Fore.RED + "Weather API Error!")
    except Exception as e:
        print(Fore.RED + "Error:", e)

# ===== Extra Features =====
def extra_features(city):
    print(Fore.CYAN + "\n🛠️ Extra Options:")
    print("  [1] Tomorrow Forecast")
    print("  [2] Satellite View")
    print("  [3] SOS Alert")
    extra = input("Enter Option or press Enter to skip: ").strip()
    if extra == "1":
        os.system(f"python forecast.py {city}")
    elif extra == "2":
        os.system("python satellite.py")
    elif extra == "3":
        os.system("python sos_alert.py")

# ===== Offline Fallback (Basic) =====
def offline_notice(city):
    print(Fore.RED + "\n🔌 You are offline! Showing saved fallback data...")
    print(Fore.YELLOW + f"\n[{city}]: ☀️ Moderate Weather | 29°C | Humidity 75% | Wind 8 km/h\n")
    print(Fore.GREEN + "📌 Forecast: Tomorrow partly cloudy. No rain chance.")

# ===== Main =====
def main():
    os.system("clear")
    load_banner()
    print(Fore.GREEN + "\n🌐 Welcome to BDLiveWeather!\n")
    districts = load_districts()
    if not districts:
        return
    selected = select_district(districts)
    print(Fore.CYAN + f"\n[✔] You selected: {selected}")

    # Colorful Time & Date
    now = datetime.now()
    print(Fore.MAGENTA + f"\n🕒 Date: {now.strftime('%Y-%m-%d')} | Time: {now.strftime('%I:%M:%S %p')}")

    try:
        requests.get("https://google.com", timeout=5)
        get_weather(selected)
        extra_features(selected)
    except:
        offline_notice(selected)

if __name__ == "__main__":
    main()
