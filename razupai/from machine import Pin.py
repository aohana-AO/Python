from machine import Pin
import utime
 
led_red=Pin(16,Pin.OUT)


while True:
    led_red.value(1)
    utime.sleep(0.1)
    led_red.value(0)
    utime.sleep(0.1)