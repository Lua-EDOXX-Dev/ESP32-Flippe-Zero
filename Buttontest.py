from machine import Pin, SPI
import time

hoch = Pin(5, Pin.IN, Pin.PULL_UP)
runter = Pin(7, Pin.IN, Pin.PULL_UP)
ok = Pin(41, Pin.IN, Pin.PULL_UP)
zurueck = Pin(39, Pin.IN, Pin.PULL_UP)

print("EDOXX TOOL - Button Test")

while True:

    if hoch.value() == 0:
        print("HOCH")
        time.sleep_ms(300)

    if runter.value() == 0:
        print("RUNTER")
        time.sleep_ms(300)

    if ok.value() == 0:
        print("OK")
        time.sleep_ms(300)

    if zurueck.value() == 0:
        print("ZURUECK")
        time.sleep_ms(300)