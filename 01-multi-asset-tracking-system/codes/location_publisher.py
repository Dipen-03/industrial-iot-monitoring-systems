import paho.mqtt.client as mqtt
import time
import json # Used to correctly format the JSON payload

# --- CONFIGURATION (Ensure this matches your Node-RED setup) ---
mqttBroker = "test.mosquitto.org"
TOPIC = "Walking01/status/location"
# IMPORTANT: CHANGE 'DipenLocationTracker' to your unique name for the map marker
DEVICE_NAME = "DipenLocationTracker" 
# Ensure your CLIENT_ID is unique every time you run the script
CLIENT_ID = f'LocationSimulator_{time.time()}' 

# Starting Coordinates (Near Helsinki, as per assignment)
sensorLat = 60.16920526 
sensorLon = 24.95115530

# Movement steps (As per assignment instructions)
lat_step = 0.0000056  # one step north
lon_step = 0.0000123  # one step east
interval = 1         # 1 second interval
i = 1

# --- MQTT Connection and Publishing Loop ---
client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311, clean_session=True)

try:
    print(f"Connecting to broker: {mqttBroker}")
    client.connect(mqttBroker, port=1883)
except Exception as e:
    print(f"Connection failed: {e}")
    exit()

print(f"Starting simulation on topic: {TOPIC}")

while i < 51: 
    # Update coordinates for movement simulation
    sensorLat = sensorLat + lat_step
    sensorLon = sensorLon + lon_step
    sensorEpoch = int(time.time()) 
    
    # --- Create the Payload Dictionary ---
    location_data = {
        # 'name' is REQUIRED by the worldmap node
        "name": DEVICE_NAME, 
        "time": str(time.ctime()),
        "epoch": sensorEpoch,
        # Round the coordinates for cleaner data
        "lat": round(sensorLat, 8),
        "lon": round(sensorLon, 8)
    }

    # Convert the Python dictionary into a correct JSON string
    payload = json.dumps(location_data)
    
    # Publish the payload
    client.publish(TOPIC, payload, qos=0)
    
    print(f"Published {i} (Lat: {round(sensorLat, 8)}, Lon: {round(sensorLon, 8)})")
    
    i = i + 1
    time.sleep(interval) 

client.disconnect()
print("Finished publishing and disconnected.")