from machine import Pin, SPI, PWM
import st7789 as ST
import time

spi = SPI(
    2,
    baudrate=10_000_000,
    polarity=0,
    phase=0,
    sck=Pin(12),
    mosi=Pin(11)
)

display = ST.ST7789(
    spi,
    240, 280, #Größe
    reset=Pin(8, Pin.OUT),
    dc=Pin(9, Pin.OUT),
    cs=Pin(10, Pin.OUT),
    rotation=0,
    x_offset=0,
    y_offset=20
)

display.init() #display initialiesieren
display.fill(ST.MAGENTA) #Bildschirm füllen mit bestimmter farbe

    
#Text anzeigen lassen
def main_menu():
    display.fill(ST.MAGENTA)
    display.text("""
          (==============)   
            (EDOXX TOOL)
          (==============)
          ([1] IR Remote)
          ([2] WiFi)
          ([3] Network)
          ([4] RFID/NFC)
          ([5] 433 MHz)
          ([6] Recon)
          ([7] Settings)
          ([8] Hardware) """, -110, 10, ST.WHITE, background=None, size=2)


menu = ["IR Remote", "WiFi", "Network Menu", "RFID / NFC",
         "433 MHz", "Tools", "Recon", "Settings", "Hardware"]

ir_menu = ["TV Remote", "IR Scanner", "Send IR Code", "Learn IR Code", "Saved Remotes"]

main_menu()
buzzer_pin = Pin(6, Pin.OUT)
buzzer_pin.value(0)
buzzer = PWM(buzzer_pin)
buzzer.duty_u16(0)
auswahl = 1

hoch = Pin(5, Pin.IN, Pin.PULL_UP)
runter = Pin(15, Pin.IN, Pin.PULL_UP)
ok = Pin(41, Pin.IN, Pin.PULL_UP)
zurueck = Pin(39, Pin.IN, Pin.PULL_UP)

#Menues

display.text(str(auswahl), 180, 220, ST.WHITE, background=ST.MAGENTA, size=3)

#IR Remote Menu
def ir_remote():
    auswahl_ir_remote = 1
    
    while True:
        display.text("""
        (==============)   
          (IR MENU)
        (==============)
        [1] TV Remote
        [2] IR Scanner
        [3] Send IR Code
        [4] Learn IR Code
        [5] Saved Remotes""", -80, 10, ST.WHITE, background=None, size=2)
        
        if zurueck.value() == 0:
            display.fill(ST.MAGENTA)
            main_menu()
            break
        
        #Begrenzen der auswahl
        if auswahl_ir_remote < 1:
            auswahl_ir_remote = 1
    
        if auswahl_ir_remote > 5:
            auswahl_ir_remote = 5
    
        #Knöpfe abfragen für auswahl
        if runter.value() == 0: 
            auswahl_ir_remote += 1
            time.sleep_ms(300)
            display.text(str(auswahl_ir_remote), 180, 220, ST.WHITE, background=ST.MAGENTA, size=3)
            time.sleep_ms(300)
        
        if hoch.value() == 0:
            auswahl_ir_remote -= 1
            time.sleep_ms(300)
            display.text(str(auswahl_ir_remote), 180, 220, ST.WHITE, background=ST.MAGENTA, size=3)
            time.sleep_ms(300)
        
    #OK knopf
        if ok.value() == 0:
            if auswahl_ir_remote == 1:
                display.fill(ST.MAGENTA)
                time.sleep(1)
                ir_remote()
                time.sleep_ms(100)
                auswahl_ir_remote = 1
            elif auswahl_ir_remote == 2:
                display.fill(ST.MAGENTA)
                time.sleep(1)
                ir_scanner()
                time.sleep_ms(100)
                auswahl_ir_remote = 1
            elif auswahl_ir_remote == 3:
                display.fill(ST.MAGENTA)
                time.sleep(1)
                network_menu()
                time.sleep_ms(100)
                auswahl_ir_remote = 1
            elif auswahl_ir_remote == 4:
                display.fill(ST.MAGENTA)
                time.sleep(1)
                nfc_menu()
                time.sleep_ms(100)
                auswahl_ir_remote = 1
            elif auswahl_ir_remote == 5:
                display.fill(ST.MAGENTA)
                time.sleep(1)
                mhz_menu()
                time.sleep_ms(100)
                auswahl_ir_remote = 1
            
            time.sleep_ms(300)
        
def wifi_menu():
    
    while True:
        display.text("""
        (==============)   
          (WIFI MENU)
        (==============)
        [1] Wifi Scanner
        [2] Saved Networks
        [3] Network Info
        [4] Signal Strength
        [5] Security Info
        [5] AP Flood """, -80, 10, ST.WHITE, background=None, size=2)
    
        if zurueck.value() == 0:
            display.fill(ST.MAGENTA)
            main_menu()
            break
        
def network_menu():
    
    while True:
        display.text("""
        (==============)   
         (NETWORK MENU)
        (==============)
        [1] Ping
        [2] DNS Lookup
        [3] IP Info
        [4] Host Scanner
        [5] Port Scanner """, -80, 10, ST.WHITE, background=None, size=2)
        
        if zurueck.value() == 0:
            display.fill(ST.MAGENTA)
            main_menu()
            break
    
def nfc_menu():
    
    while True:
        display.text("WIP", 100, 100, ST.WHITE, background=None, size=2)
        
        if zurueck.value() == 0:
            display.fill(ST.MAGENTA)
            main_menu()
            break
    
def mhz_menu():
    
    while True:
        display.text("WIP",-80, 10, ST.WHITE, background=None, size=2)
        
        if zurueck.value() == 0:
            display.fill(ST.MAGENTA)
            main_menu()
            break

def recon_menu():
    
    while True:
        display.text("""
        (==============)   
          (RECON MENU)
        (==============)
        [1] Host Info
        [2] DNS Info
        [3] IP Info
        [4] Service Scan
        [5] Device Scan """, -80, 10, ST.WHITE, background=None, size=2)
        
        if zurueck.value() == 0:
            display.fill(ST.MAGENTA)
            main_menu()
            break
        
def settings_menu():
    
    while True:
        display.text("""
        (==============)   
           (SETTINGS)
        (==============)
        [1] Brightness
        [2] Sound
        [3] Theme
        [4] Device Name
        [5] About """, -80, 10, ST.WHITE, background=None, size=2)
        
        if zurueck.value() == 0:
            display.fill(ST.MAGENTA)
            main_menu()
            break
    
def hardware_menu():
    
    while True:
        display.text("""
        (==============)   
           (HARDWARE)
        (==============)
        [1] GPIO Test
        [2] Button Test
        [3] Joystick Test
        [4] Display Test
        [5] Free Space
        [6] Buzzer Test """, -80, 10, ST.WHITE, background=None, size=2)
        
        if zurueck.value() == 0:
            display.fill(ST.MAGENTA)
            main_menu()
            break
        
def buzzer_test():
    display.text("""
    (==============)   
      (Testing...)
    (==============) """, -80, 50, ST.WHITE, background=None, size=2)
    buzzer.freq(2000)
    buzzer.duty_u16(1000)
    time.sleep(1)
    buzzer.duty_u16(0)
    buzzer.deinit()
    time.sleep(3)
    display.fill(ST.MAGENTA)
    hardware_menu()
    
def button_test():
    display.text("""
    (==============)   
      (Testing...)
    (==============) """, -80, 50, ST.WHITE, background=None, size=2)
     
    while True:

        if hoch.value() == 0:
            display.text("Up Works", -80, 50, ST.WHITE, background=None, size=2)
            time.sleep_ms(300) 

        if runter.value() == 0:
            display.text("Down Works", -80, 60, ST.WHITE, background=None, size=2)
            time.sleep_ms(300)

        if ok.value() == 0:
            display.text("Ok Works", -80, 70, ST.WHITE, background=None, size=2)
            time.sleep_ms(300)

        if zurueck.value() == 0:
            display.text("Back Works", -80, 80, ST.WHITE, background=None, size=2)
            time.sleep_ms(300)
    
    
def ir_scanner():
    
    from machine import Pin, time_pulse_us
    import time

    rx = Pin(17, Pin.IN)
    time.sleep(2)

    display.text("Jetzt eine Fernbedienungstaste druecken!", 10, 80, ST.WHITE, background=None, size=2)

    # Auf einen LOW-Puls warten
    start = time.ticks_ms()
    while rx.value() == 1:
        if time.ticks_diff(time.ticks_ms(), start) > 10000:
            print("Kein Signal erkannt.")
            raise SystemExit

    pulses = []

    # Signalabschnitte aufnehmen
    for i in range(100):
        low = time_pulse_us(rx, 0, 20000)
        if low < 0:
            break

        high = time_pulse_us(rx, 1, 20000)
        if high < 0:
            break

        pulses.append((low, high))
    display.text("Aufnahme fertig!", 10, 100, ST.WHITE, background=None, size=2)
    display.text("Anzahl Pulse:", len(pulses), 10, 120, ST.WHITE, background=None, size=2)




while True:
    #Begrenzen
    if auswahl < 1:
        auswahl = 1
    
    if auswahl > 8:
        auswahl = 8
    
    #Knöpfe abfragen
    if runter.value() == 0: 
        auswahl += 1
        time.sleep_ms(300)
        display.text(str(auswahl), 180, 220, ST.WHITE, background=ST.MAGENTA, size=3)
        time.sleep_ms(300)
        
    if hoch.value() == 0:
        auswahl -= 1
        time.sleep_ms(300)
        display.text(str(auswahl), 180, 220, ST.WHITE, background=ST.MAGENTA, size=3)
        time.sleep_ms(300)
        
    if ok.value() == 0:
        if auswahl == 1:
            display.fill(ST.MAGENTA)
            time.sleep(1)
            ir_remote()
            display.text(str(auswahl_ir_remote), 180, 220, ST.WHITE, background=ST.MAGENTA, size=3)
            time.sleep_ms(100)
            auswahl = 1
        elif auswahl == 2:
            display.fill(ST.MAGENTA)
            time.sleep(1)
            wifi_menu()
            time.sleep_ms(100)
            auswahl = 1
        elif auswahl == 3:
            display.fill(ST.MAGENTA)
            time.sleep(1)
            network_menu()
            time.sleep_ms(100)
            auswahl = 1
        elif auswahl == 4:
            display.fill(ST.MAGENTA)
            time.sleep(1)
            nfc_menu()
            time.sleep_ms(100)
            auswahl = 1
        elif auswahl == 5:
            display.fill(ST.MAGENTA)
            time.sleep(1)
            mhz_menu()
            time.sleep_ms(100)
            auswahl = 1
        elif auswahl == 6:
            display.fill(ST.MAGENTA)
            time.sleep(1)
            recon_menu()
            time.sleep_ms(100)
            auswahl = 1
        elif auswahl == 7:
            display.fill(ST.MAGENTA)
            time.sleep(1)
            settings_menu()
            time.sleep_ms(100)
            auswahl = 1
        elif auswahl == 8:
            display.fill(ST.MAGENTA)
            time.sleep(1)
            hardware_menu()
            time.sleep_ms(100)
            auswahl = 1
            
        time.sleep_ms(300)
        
