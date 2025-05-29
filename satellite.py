#!/usr/bin/env python3

import webbrowser

def show_satellite():
    print("\n🌐 Opening Satellite View in browser...")
    url = "https://www.satelliteview.co/?map=BD"
    webbrowser.open(url)

if __name__ == "__main__":
    show_satellite()
