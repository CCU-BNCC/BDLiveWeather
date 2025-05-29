#!/usr/bin/env python3

import requests
import sys

def get_forecast(city):
    try:
        url = f"https://wttr.in/{city}?m&format=3"
        print("\n[📅 Tomorrow's Forecast]".center(40, "-"))
        print(f"🔮 Forecast: {url.replace('?m&format=3','')}?1")
        response = requests.get(f"https://wttr.in/{city}?1")
        if response.status_code == 200:
            print(response.text)
        else:
            print("⚠️ Forecast API error!")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python forecast.py <city>")
    else:
        get_forecast(sys.argv[1])
