#Made by Erik
#For ESP32 Vroom1 for Flipper Zero imitation
#Only For Ethical Stuff, i´m not responsible for anything

#imports
from machine import Pin
import time

#git add Flipper.py
#git commit -m "Beschreibung der Änderung"
#git push

#Buttons
hoch = Pin(5, Pin.IN, Pin.PULL_UP)
runter = Pin(7, Pin.IN, Pin.PULL_UP)
ok = Pin(41, Pin.IN, Pin.PULL_UP)
zuruck = Pin(39, Pin.IN, Pin.PULL_UP)

#Main Menu
menu = ["IR Remote", "WiFi", "Network", "RFID"]

auswahl = 0

def main_menu():
    print("====================")   
    print("     EDOXX TOOL")
    print("====================")
    print("[1] IR Remote")
    print("[2] WiFi")
    print("[3] Network Menu")
    print("[4] RFID / NFC")
    print("[5] 433 MHz")
    print("[6] Tools")
    print("[7] Recon")
    print("[8] Settings")
    print("[9] Hardware")

    selection1 = input()

    if selection1 == "1":
        ir_remote()
    elif selection1 == "2":
        wifi_menu()
    elif selection1 == "3":
        network_menu()
    elif selection1 == "4":
        rfid_menu()
    elif selection1 == "5":
        mhz_menu()
    elif selection1 == "6":
        recon_menu()
    elif selection1 == "7":
        settings_menu()
    elif selection1 == "8":
        hardware_menu()

#IR Remote menu
def ir_remote():
    while True:
        print("[1] TV Remote")
        print("[2] IR Scanner")
        print("[3] Send IR Code")
        print("[4] Learn IR Code")
        print("[5] Saved Remotes")
        print("[0] Back")
        selection = input("Auswahl: ")

        if selection == "1":
            print("TV Remote")
        elif selection == "2":
            print("IR Scanner")
        elif selection == "3":
            print("Send IR Code")
        elif selection == "4":
            print("Learn IR Code")
        elif selection == "5":
            print("Saved Remotes")
        elif selection == "0":
            break

#Wifi Menu
def wifi_menu():
    print("[1] Wifi Scanner")
    print("[2] Saved Networks")
    print("[3] Network Info")
    print("[4] Signal Strength")
    print("[5] Security Info")
    print("[5] AP Flood")
    selection = input()

def rfid_menu():
    print("[1] RFID Scanner")
    print("[2] Read UID")
    print("[3] Read Tag")
    print("[4] Write Tag")
    print("[5] Saved Tags")

def mhz_menu():
    print("[1] RF Scanner")
    print("[2] Learn Signal")
    print("[3] Analyze Signal")
    print("[4] Send Signal")
    print("[5] Saved Signals")

def network_menu():
    print("[1] Ping")
    print("[2] DNS Lookup")
    print("[3] IP Info")
    print("[4] Host Scanner")
    print("[5] Port Scanner")

def recon_menu():
    print("[1] Host Info")
    print("[2] DNS Info")
    print("[3] IP Info")
    print("[4] Service Scan")
    print("[5] Device Scan")

def hardware_menu():
    print("[1] GPIO Test")
    print("[2] Button Test")
    print("[3] Joystick Test")
    print("[4] Display Test")
    print("[5] Buzzer Test")

def settings_menu():
    print("[1] Brightness")
    print("[2] Sound")
    print("[3] Theme")
    print("[4] Device Name")
    print("[5] About")

#Button test

def button_test():
    if hoch.value() == 0:
        print("HOCH")

    if runter.value() == 0:
        print("RUNTER")

    if ok.value() == 0:
        print("OK")

    if zuruck.value() == 0:
        print("ZURUECK")

    time.sleep_ms(100)

    #Muss ganz unten sein
while True:
    main_menu()
