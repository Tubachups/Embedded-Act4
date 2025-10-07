import RPi.GPIO as GPIO
import time

VIBRATION_PIN = 20
last_vibration_time = 0
LED_PIN = 12


GPIO.setmode(GPIO.BCM)
GPIO.setup(VIBRATION_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)  


def get_vibration_data():
    global last_vibration_time
    raw_state = GPIO.input(VIBRATION_PIN)

    if raw_state == GPIO.HIGH:
        last_vibration_time = time.time()

    # If no HIGH detected for 1 second → assume no vibration
    if time.time() - last_vibration_time < 1:
        GPIO.output(LED_PIN, GPIO.HIGH)
        return {
            "detected": True,
            "message": "⚠️ Vibration detected!"
        }
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        return {
            "detected": False,
            "message": "No vibration detected."
        }
