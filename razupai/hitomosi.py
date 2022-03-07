import machine
from machine import Pin
import utime

led = Pin(25, Pin.OUT)
led1=Pin(16,Pin.OUT)
led2=Pin(17,Pin.OUT)
led3=Pin(18,Pin.OUT)
led4=Pin(19,Pin.OUT)
led5=Pin(20,Pin.OUT)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
reading = sensor_temp.read_u16() * conversion_factor
temperature00 = 27 - (reading - 0.706)/0.001721
print(temperature00)
led1.value(1)
led2.value(1)
led3.value(1)
led4.value(1)
led5.value(1)
led.value(1)

while True:
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    if temperature < temperature00-3:
        
        led.value(0)
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        

    elif temperature <temperature00-0.9:
        led.value(1)
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        
        
    elif temperature <temperature00-0.7:
        
        led.value(1)
        led1.value(1)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        
    elif temperature <temperature00-0.5:
        
        led.value(1)
        led1.value(1)
        led2.value(1)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        
    elif temperature <temperature00-0.3:
        led.value(1)
        led1.value(1)
        led2.value(1)
        led3.value(1)
        led4.value(0)
        led5.value(0)
    elif temperature <temperature00-0.1:
        led.value(1)
        led1.value(1)
        led2.value(1)
        led3.value(1)
        led4.value(1)
        led5.value(0)
        
    else:
        
        led.value(1)
        led1.value(1)
        led2.value(1)
        led3.value(1)
        led4.value(1)
        led5.value(1)
    
    

    utime.sleep(1)