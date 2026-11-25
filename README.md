# Students

- Liam Tuite - c21447352
- Oisin Kiely - c21501436
- Providence Obiozor - c20499732

# Lab 9 – Protocol Buffers

## Overview

This project implements MQTT communication between two Raspberry Pi Pico W devices using Protocol Buffers for message encoding and decoding.

## System

- **Publisher:** Reads temperature data from the Pico's internal temperature sensor and publishes it via MQTT.
- **Subscriber:** Receives temperature readings, decodes the Protocol Buffers messages and controls an LED based on the temperature.
- **MQTT Broker:** A Raspberry Pi running Mosquitto, which handles communication between the publisher and subscriber.

## MQTT Configuration

- **Broker:** Raspberry Pi running Mosquitto
- **Port:** 8080
- **Topic:** `temp/pico`

## Files

- `publisher.py` – MQTT publisher implementation.
- `subscriber.py` – MQTT subscriber implementation.
- `temperature.proto` – Protocol Buffers message schema.
- `temperature_upb2.py` – Generated MicroPython message classes.
- `uprotobuf.py` – MicroPython Protocol Buffers library.
- `mosquitto.conf` – MQTT broker configuration.

## Setup

Update the Wi-Fi name, password and broker IP address in both Python files before running.

Run the Mosquitto broker on the Raspberry Pi, then run the subscriber and publisher on their respective Pico W devices.
