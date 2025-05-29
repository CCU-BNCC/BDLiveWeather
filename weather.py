#!/usr/bin/env python3

# ==========================================================
#              BDLiveWeather Main Script 🇧🇩
#              Made in MD Abdullah
# ==========================================================

import os
import requests
from datetime import datetime
from termcolor import colored
import inquirer

# === Load Banner ===
def load_banner():
    if os.path.exists("banner.txt"):
        with open("banner.txt", "r") as b:
            print(b.read())
    else:
        print("==== BDLiveWeather ====")

# === Load District List for Menu ===
def get_district_list():
    if os.path.exists("districts.txt"):
        with open("districts.txt", "r") as d:
            return [line.strip().split('. ', 1)[1] for line in d.readlines()]
    else:
        return []

# === Check Internet ===
def is_connected():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except:
        return False

# === Get Live Weather ===
def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=%l:+%c+%t+%h+%w\n"
        response = requests.get(url)
        if response.status_code == 200:
            print("\n[Live Weather]".center(40, "-"))
            print(response.text)
        else:
            print("⚠️ Weather API Error!")
    except Exception as e:
        print("❌ Error:", e)

# === Main Menu ===
def main():
    os.system("clear")
    load_banner()

    print(colored("📍 Select Your District:\n", "cyan"))

    district_list = get_district_list()
    if not district_list:
        print("❌ District list not found!")
        return

    question = [
        inquirer.List("district",
                      message="Select a District",
                      choices=district_list)
    ]
    answer = inquirer.prompt(question)
    choice = answer['district']

    print(colored(f"\n[INFO] Getting live weather for: {choice}", "yellow"))

    now = datetime.now()
    print(colored("📅 Current Date: ", "green") + colored(now.strftime("%Y-%m-%d"), "white"))
    print(colored("⏰ Current Time: ", "green") + colored(now.strftime("%H:%M:%S"), "white"))

    if is_connected():
        get_weather(choice)
    else:
        print(colored("\n⚠️ No internet connection! Showing offline fallback.\n", "red"))
        print(f"Offline weather info for {choice} is not available.")
        print("Please connect to the internet and try again.")

# === Run Script ===
if __name__ == "__main__":
    main()
