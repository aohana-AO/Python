import csv
import machine
from machine import Pin
import utime




file = open('new.csv', 'w')  
w = csv.writer(file)
led = Pin(25, Pin.OUT)
i=0
while i>11:
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    if temperature > 21 :
        led.value(1)
    else:
        led.value(0)
    utime.sleep(2)
    i+=1
    w.writerow([temperature])

file.close()


