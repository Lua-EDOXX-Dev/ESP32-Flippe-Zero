#Made by Erik
#For ESP32 Vroom1 for Flipper Zero imitation
#Only For Ethical Stuff, i´m not responsible for anything

#Main Menu
def main_menu():
    print("====================")   
    print("     EDOXX TOOL")
    print("====================")
    print("[1] IR Remote")
    print("[2] WiFi")
    print("[3] Tools")
    print("[4] Settings")
    print("[5] Exit")

    selection1 = input()
    if selection1 == "1":
        print("Option 1")
    elif selection1 == "2":
        print("Option 2")
    elif selection1 == "3":
        print("Option 3")
    elif selection1 == "4":
        print("Option 4")

while True:
    main_menu()

def 