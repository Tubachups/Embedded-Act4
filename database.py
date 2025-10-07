import sqlite3
from datetime import datetime

DB_NAME = "sensor_readings.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS sensor_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gas_status TEXT NOT NULL,
            vibration_status TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_reading(gas_status, vibration_status):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("""
        INSERT INTO sensor_readings (gas_status, vibration_status, timestamp)
        VALUES (?, ?, ?)
    """, (gas_status, vibration_status, timestamp))
    conn.commit()
    conn.close()

def get_readings(limit=20):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        SELECT gas_status, vibration_status, timestamp
        FROM sensor_readings
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))
    rows = c.fetchall()
    conn.close()
    return rows
