# Industrial IoT & Real-Time Monitoring Portfolio
## MQTT-NodeRED-Monitoring-Solutions  
This repository contains a collection of university-level Industrial IoT projects focused on MQTT communication, real-time data streaming, and visualization using Node-RED.

The projects demonstrate practical implementation of publish/subscribe architecture, structured topic hierarchy design, and real-time monitoring dashboards.

---

#  Repository Structure

This main repository contains three independent IoT projects:

```
MQTT-NodeRED-Monitoring-Solutions/
│
├── 01-multi-asset-tracking-system/
├── 02-environmental-sensor-dashboard/
├── 03-mqtt-topic-architecture/
└── README.md
```

---

#  Projects Overview

##  Multi-Asset Tracking System  
 [01-multi-asset-tracking-system](./01-multi-asset-tracking-system)

**Technologies Used:**
- Python
- MQTT (Paho-MQTT)
- Node-RED
- WorldMap Node
- JSON

**Project Description:**

This project simulates a real-time GPS tracking system for multiple moving assets.

Two virtual devices are implemented:
- A Person Tracker
- A Rescue Vehicle

Both devices publish location data to an MQTT broker. Node-RED processes the incoming messages and visualizes them on a live map.

**Key Features:**
- Real-time GPS simulation
- MQTT publish/subscribe architecture
- Conditional routing using Node-RED Switch node
- Dynamic marker styling (color and icon differentiation)
- Multi-device tracking on a single topic

**Real-World Application Example:**
Emergency response coordination system for monitoring field personnel and vehicles in real time.

---

##  Environmental Sensor Dashboard  
 [02-environmental-sensor-dashboard](./02-Environmental-Dashboard)

**Technologies Used:**
- Python (Paho-MQTT)
- JSON
- Node-RED Dashboard
- MQTT Broker

**Project Description:**

This project demonstrates an end-to-end IoT data pipeline for environmental monitoring.

A Python script simulates temperature and humidity sensor data, encodes it in JSON format, and publishes it to an MQTT topic. Node-RED subscribes to the data and displays it on a web-based dashboard using gauges and visual indicators.

**Key Features:**
- Structured JSON data serialization
- MQTT topic-based communication
- Real-time dashboard visualization
- Calibrated UI components (gauges and indicators)

**Real-World Application Example:**
Industrial facility monitoring system for tracking environmental conditions in storage areas or production units.

---

##  Industrial MQTT Topic Architecture  
 [03-mqtt-topic-architecture](./03-Mqtt-Topic-Architecture)

**Technologies Used:**
- MQTT Explorer
- Node-RED
- MQTT Wildcards (+ and #)

**Project Description:**

This project focuses on designing and validating an industrial-grade MQTT topic hierarchy for scalable communication in factory environments.

The system demonstrates the use of:
- Single-level wildcard (+)
- Multi-level wildcard (#)

These are used to manage factory-wide events and enable flexible message subscriptions.

**Key Features:**
- Hierarchical topic design
- Wildcard-based subscription logic
- Scalable industrial messaging architecture
- Validation using MQTT Explorer and Node-RED

**Real-World Application Example:**
Smart factory communication system for monitoring machines, production lines, and facility-wide alerts.

---

# Core Skills Demonstrated

### Programming
- Python for IoT device simulation
- JSON data structuring

### Communication Protocols
- MQTT publish/subscribe model
- Topic hierarchy design
- Wildcard-based filtering
- Broker communication

### Tools & Platforms
- Node-RED
- Node-RED Dashboard
- WorldMap Node
- MQTT Explorer

---

#  Learning Outcomes

Through these projects, the following Industrial IoT concepts were implemented and validated:

- Real-time data streaming
- Multi-device communication over MQTT
- Event-driven architecture
- Structured topic design for scalability
- Live monitoring dashboards
- Geospatial data visualization

---

#  Academic Context

These projects were developed as part of university coursework in Industrial IoT and real-time monitoring systems.

The objective was to design, implement, and validate complete IoT communication pipelines using industry-standard tools and protocols.

---
