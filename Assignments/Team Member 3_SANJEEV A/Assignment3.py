
import Button, LED , TrafficLights
import time
import sleep
led = LED(25)
lights = TrafficLights(25, 8, 7)
lights.on()
lights.off()
light.blink()
while True:
    lights.blink(5, 5)
    button.wait_for_press()
    led.on()
    button.wait_for_release()
    led.off()
    
    lights.blink()
    button.wait_for_press()
    lights.off()
    button.wait_for_release()
    
    lights.green.on()
    sleep(1)
    lights.yello.on()
    sleep(1)
    lights.red.on()
    sleep(1)
    lights.off()
    
