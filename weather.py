#!/usr/bin/env python3

# BDLiveWeather - Made in MD Abdullah 🇧🇩

import os
import time
import curses
import requests
from datetime import datetime
from termcolor import colored

# === Load Banner ===
def load_banner():
    if os.path.exists("banner.txt"):
        with open("banner.txt", "r") as b:
            print(b.read())
    else:
        print("==== BDLiveWeather ====")

# === Load Districts ===
def load_districts():
    if os.path.exists("districts.txt"):
        with open("districts.txt", "r") as d:
            return [line.strip() for line in d if line.strip()]
    else:
        print("District list not found!")
        return []

# === Get Live Weather ===
def get_weather(city):
    try:
        print(colored("\n[Live Weather]".center(40, "-"), "cyan"))
        url = f"https://wttr.in/{city}?format=%l:+%c+%t+%h+%w\n"
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
        else:
            print("Weather API Error!")
    except Exception as e:
        print("Error:", e)

# === GUI Menu ===
def menu(stdscr, districts):
    curses.curs_set(0)
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    selected = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 2, "Select District (↑↓ and Enter):", curses.A_BOLD)

        for i, district in enumerate(districts):
            if i >= h - 3:
                break  # Don't overflow terminal height
            if i == selected:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(i+2, 2, f"> {district}")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(i+2, 2, f"  {district}")
        key = stdscr.getch()

        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(districts) - 1:
            selected += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            return districts[selected]

# === Select from GUI ===
def select_district(districts):
    return curses.wrapper(lambda stdscr: setup_and_menu(stdscr, districts))

def setup_and_menu(stdscr, districts):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    return menu(stdscr, districts)

# === Main ===
def main():
    os.system("clear")
    load_banner()

    print(colored("\n🗓️ Date: " + datetime.now().strftime("%Y-%m-%d"), "green"))
    print(colored("⏰ Time: " + datetime.now().strftime("%H:%M:%S"), "yellow"))

    districts = load_districts()
    if not districts:
        return

    print("\n🎯 Use ↑ ↓ to select your district:\n")
    time.sleep(1)
    selected = select_district(districts)

    print(colored(f"\n🔍 Getting weather for: {selected}", "magenta"))
    get_weather(selected)

    print("\n🛠️ Extra Options:")
    print("  [1] Tomorrow Forecast")
    print("  [2] Satellite View")
    print("  [3] SOS Alert")
    extra = input("Enter Option or press Enter to skip: ").strip()

    if extra == "1":
        os.system(f"python forecast.py {selected}")
    elif extra == "2":
        os.system("python satellite.py")
    elif extra == "3":
        os.system("python sos_alert.py")

# === Run Script ===
if __name__ == "__main__":
    main()
