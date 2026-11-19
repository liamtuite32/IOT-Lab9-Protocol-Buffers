## Lab 8 - IOT

- Liam Tuite - c21447352
- Oisin Kiely - c21501436


## Project Description
A simple IoT temperature monitoring system using two Raspberry Pi Pico W boards communicating through MQTT. The system monitors temperature and uses an LED to indicate when the temperature reaches a specified threshold.

## System Components
- **Raspberry Pi Pico W (Publisher):** Reads temperature data using its onboard temperature sensor.
- **Raspberry Pi Pico W (Subscriber):** Receives temperature readings and controls an LED.
- **Raspberry Pi:** Hosts the Mosquitto MQTT broker.
- **Wi-Fi Network:** Connects the devices for communication.

## Program Files
- **Publisher.py:** Reads the onboard temperature sensor, converts the reading into Celsius and publishes it to the MQTT broker every second.
- **Subscriber.py:** Receives temperature readings and turns an LED connected to GPIO 15 ON or OFF depending on the temperature.
- **Mosquitto.conf:** Contains the MQTT broker configuration settings.

## System Behaviour
1. Both Pico W boards connect to the Wi-Fi network.
2. The publisher reads the temperature every second.
3. Temperature readings are sent to the MQTT broker.
4. The subscriber receives and displays the readings.
5. If the temperature is 25°C or above, the LED turns ON.
6. If the temperature is below 25°C, the LED turns OFF.

## MQTT Configuration
The project uses the Mosquitto MQTT broker hosted on a Raspberry Pi.

- **Port:** 1883
- **Protocol:** MQTT
- **Listener:** 0.0.0.0 (accepts connections on all network interfaces)
- **Authentication:** Anonymous connections enabled
- **Topic:** `temperature/pico`

Both Pico W boards connect to the broker using its IP address.

## Testing
The system is tested by running both Python programs simultaneously. The publisher sends temperature readings every second, while the subscriber displays the received values.

The LED is tested against the 25°C threshold:
- **25°C or above:** LED ON.
- **Below 25°C:** LED OFF.

Successful message reception and LED control demonstrate that MQTT communication is working correctly.
