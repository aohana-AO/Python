import machine
from machine import Pin
import utime
led_red=Pin(16,Pin.OUT)
while True:
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    if temperature > 20 :
        led_red.value(1)
    else:
        led_red.value(0)
    utime.sleep(2)