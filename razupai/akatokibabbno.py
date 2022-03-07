import machine, time
# Pico の LED を操作する
led = machine.Pin(25, machine.Pin.OUT)
led_red = machine.Pin(16, machine.Pin.OUT)

# 繰り返す
while True:
    led.high() # LEDを点灯
    time.sleep(0.5)
    led_red.high() # LEDを点灯
    time.sleep(0.5)
    
    led.low()  # LEDを消灯
    time.sleep(0.5)
    led_red.low() # LEDを点灯
    time.sleep(0.5)