#!/usr/bin/env python3
"""
Luminosity Data Publisher

This script simulates a luminosity sensor by generating random luminance data
and publishing it to an MQTT broker at regular intervals.

Requirements:
- Python 3
- paho-mqtt

Usage:
1. Ensure your MQTT broker (e.g., Mosquitto) is running on localhost.
2. Install dependencies:
   pip install -r requirements.txt
3. Run the script:
   python luminosity_publisher.py
"""

import paho.mqtt.client as mqtt
import random
import time

# MQTT broker settings
BROKER_ADDRESS = "localhost"  # Change if your broker is on a different IP address
BROKER_PORT = 1883
TOPIC = "livingroom/luminosity"

def generate_luminosity():
    """
    Generate a random luminosity value.
    Range: 0 - 1000 lux (adjust as needed)
    """
    return random.uniform(0, 1000)

def main():
    # Create MQTT client instance
    client = mqtt.Client()

    # Connect to MQTT broker
    try:
        client.connect(BROKER_ADDRESS, BROKER_PORT)
        print(f"Connected to MQTT broker at {BROKER_ADDRESS}:{BROKER_PORT}")
    except Exception as e:
        print(f"Failed to connect to MQTT broker: {e}")
        return

    print("Starting luminosity data transmission...")
    try:
        while True:
            luminosity_value = generate_luminosity()
            payload = f"{luminosity_value:.2f}"  # format to 2 decimal places
            result = client.publish(TOPIC, payload)

            if result[0] == 0:
                print(f"Published luminosity: {payload} lux")
            else:
                print("Failed to publish data")
            # Wait before sending next data point
            time.sleep(5)
    except KeyboardInterrupt:
        print("Transmission stopped by user.")

if __name__ == "__main__":
    main()
