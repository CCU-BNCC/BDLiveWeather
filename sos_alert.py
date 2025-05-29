#!/usr/bin/env python3

import os
import time

def sos_alert():
    print("\n🚨 SOS ALERT SYSTEM 🚨\n")
    msg = "⚠️ গুরত্বপূর্ণ ঝড় / দুর্যোগের সতর্কতা!!!"
    for i in range(3):
        os.system("termux-vibrate -d 500")
        print("🔴", msg)
        time.sleep(1)

    print("\n📡 Visit Official Alert Website:")
    print("👉 https://www.bmd.gov.bd/")

if __name__ == "__main__":
    sos_alert()
