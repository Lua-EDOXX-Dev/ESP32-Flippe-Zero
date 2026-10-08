#Imports
from machine import Pin, PWM
import time

#Pin
buzzer = PWM(Pin(6))
#Freuquenz
buzzer.freq(2000)

#Buzzer an
buzzer.duty_u16(250)

#3 Sek warten
time.sleep(3)

#Buzzer aus
buzzer.duty_u16(0)
#PWM beenden, ressurcen freigeben
buzzer.deinit()

print("fertig")