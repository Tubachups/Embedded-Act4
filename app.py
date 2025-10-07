# app.py
from flask import Flask, render_template, jsonify
from mqgas import get_gas_data
from vibration import get_vibration_data
from buzzer import buzzer_on, buzzer_off
from database import get_readings, init_db, insert_reading  
from emailnotify import send_email_notification  

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Initialize DB on startup
init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/sensors")
def api_sensors():
    gas_data = get_gas_data()
    vibration_data = get_vibration_data()

    # Combined buzzer + email logic
    if gas_data["detected"] and vibration_data["detected"]:
        buzzer_on()
        buzzer_status = "ON"

        # Send email alert
        send_email_notification()   # ✅ call the right function name
    else:
        buzzer_off()
        buzzer_status = "OFF"

    # Store in DB
    insert_reading(
        "Detected" if gas_data["detected"] else "No Gas",
        "Detected" if vibration_data["detected"] else "No Vibration"
    )

    return jsonify({
        "gas": gas_data,
        "vibration": vibration_data,
        "buzzer": buzzer_status
    })

@app.route("/api/history")
def api_history():
    rows = get_readings(limit=50)  # get last 50 readings
    # rows = [(gas_status, vibration_status, timestamp), ...]

    gas_values = []
    vibration_values = []
    timestamps = []

    for gas, vib, ts in reversed(rows):  # reverse so oldest first
        gas_values.append(1 if "Detected" in gas else 0)
        vibration_values.append(1 if "Detected" in vib else 0)
        timestamps.append(ts)

    return jsonify({
        "timestamps": timestamps,
        "gas": gas_values,
        "vibration": vibration_values
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
