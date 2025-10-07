# buzzer.py
import RPi.GPIO as GPIO

BUZZER_PIN = 16  # your buzzer pin
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def buzzer_on():
    GPIO.output(BUZZER_PIN, GPIO.HIGH)

def buzzer_off():
    GPIO.output(BUZZER_PIN, GPIO.LOW)
