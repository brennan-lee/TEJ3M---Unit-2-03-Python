import time
import RPi.GPIO as GPIO

PIN_5 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_5, GPIO.OUT)

delay_time = 1

while True:
    GPIO.output(PIN_5, GPIO.HIGH)
    time.sleep(delay_time)
    GPIO.output(PIN_5, GPIO.LOW)
    time.sleep(delay_time)
    
    delay_time += 1  # Increase blink time by 1 second