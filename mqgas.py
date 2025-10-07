# mqgas.py
import RPi.GPIO as GPIO

# Pin where your MQ2 sensor digital output is connected
MQ2_PIN = 21   # change to your actual GPIO pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(MQ2_PIN, GPIO.IN)

def get_gas_data():
    # Digital read from MQ2
    gas_detected = GPIO.input(MQ2_PIN) == GPIO.LOW  # LOW often means triggered for MQ2 modules

    if gas_detected:
        return {
            "detected": True,
            "message": "Gas detected! (could be LPG, Methane, Propane, Hydrogen, CO, Alcohol, Smoke)"
        }
    else:
        return {
            "detected": False,
            "message": "No significant gas detected."
        }
