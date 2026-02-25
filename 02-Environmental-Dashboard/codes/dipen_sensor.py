import paho.mqtt.client as mqtt
import time
import random
import json 

# --- Configuration for Dipen ---
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC_NAME = "OutsideAir/Dipen"       # UNIQUE TOPIC
CLIENT_ID = "PythonSimAir2_Dipen"    # UNIQUE CLIENT ID

# Define the scale limits
MIN_TEMP = 0
MAX_TEMP = 40
MIN_HUM = 30
MAX_HUM = 90
NUM_READINGS = 10 
# -----------------------------

def on_connect(client, userdata, flags, rc):
    """Callback function when the client connects."""
    if rc == 0:
        print("Connected successfully to MQTT Broker.")
    else:
        print(f"Connection failed with code {rc}")

def run_simulation():
    client = mqtt.Client(client_id=CLIENT_ID, clean_session=True)
    client.on_connect = on_connect
    
    try:
        client.connect(BROKER, PORT, 60)
        # Start the network loop to handle publishing and connection logic
        client.loop_start()

        print(f"Starting simulation. Publishing to topic: {TOPIC_NAME}")
        
        for i in range(NUM_READINGS):
            # Generate random values
            sensorTemp = round(random.uniform(MIN_TEMP, MAX_TEMP), 2)
            sensorHum = round(random.uniform(MIN_HUM, MAX_HUM), 2)
            
            # Create the payload as a dictionary
            payload_dict = {
                "Temp": sensorTemp,
                "Humidity": sensorHum
            }
            
            # Convert the dictionary to a JSON string
            payload_json = json.dumps(payload_dict) 
            
            # Publish the JSON string
            client.publish(TOPIC_NAME, payload_json)
            
            print(f"Published reading {i+1}: {payload_json}")
            time.sleep(1)

        print("Simulation complete. Disconnecting.")
        client.disconnect()
        client.loop_stop()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        client.loop_stop() 

if __name__ == "__main__":
    run_simulation()