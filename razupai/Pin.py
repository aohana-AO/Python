from machine import Pin
import utime
led6 = Pin(25, Pin.OUT)
while True:
    led6.value(1)
    utime.sleep(0.1)
    led6.value(0)
    utime.sleep(0.1)