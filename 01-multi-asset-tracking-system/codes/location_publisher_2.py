import paho.mqtt.client as mqtt
import time
import json 

# --- CONFIGURATION: RESCUE VEHICLE (DEVICE 2) ---
mqttBroker = "test.mosquitto.org"
TOPIC = "Walking01/status/location"
DEVICE_NAME = "RescueTeamVehicle" 
CLIENT_ID = f'RescueSim_{time.time()}' 

# Starting Coordinates (Different area near Helsinki)
sensorLat = 60.17500000 
sensorLon = 24.96000000
lat_step = -0.0000080 # Moving slightly South
lon_step = 0.0000010  # Moving very slightly East
interval = 1 

# --- MQTT Connection and Publishing Loop ---
client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311, clean_session=True)

try:
    print(f"Connecting tracker 2 to broker: {mqttBroker}")
    client.connect(mqttBroker, port=1883)
except Exception as e:
    print(f"Connection failed: {e}")
    exit()

i = 1
print(f"Starting simulation for: {DEVICE_NAME}")

while i < 51: 
    sensorLat = sensorLat + lat_step
    sensorLon = sensorLon + lon_step
    sensorEpoch = int(time.time()) 
    
    location_data = {
        "name": DEVICE_NAME, 
        "time": str(time.ctime()),
        "epoch": sensorEpoch,
        "lat": round(sensorLat, 8),
        "lon": round(sensorLon, 8)
    }

    payload = json.dumps(location_data)
    client.publish(TOPIC, payload, qos=0)
    
    print(f"Tracker 2 Published {i} (Lat: {round(sensorLat, 8)}, Lon: {round(sensorLon, 8)})")
    
    i = i + 1
    time.sleep(interval) 

client.disconnect()
print("Tracker 2 finished publishing and disconnected.")