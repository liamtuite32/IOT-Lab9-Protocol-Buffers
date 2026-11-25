# Lab 9: Subscriber
# Liam Tuite - c21447352
# Oisin Kiely - c21501436
# Providence Obiozor - c20499732

import network
import machine
import time
from umqtt.simple import MQTTClient
from temperature_upb2 import TemperatureReading

# WiFi and MQTT Broker Configuration - Fill with correct details
WIFI_NAME= "WIFI"
WIFI_PASSWORD= "PASSWORD"
BROKER_IP = "IP_ADDRESS"

led = machine.Pin(15, machine.Pin.OUT)  
led.value(0) 

def received_message(topic, message):
    reading = TemperatureReading.decode(message)

    temperature = reading.temperature

    print("Received temperature:", temperature)
    print("Publisher ID:", reading.publisher_id)
    print("Time:", reading.timestamp.hour,
          reading.timestamp.minute,
          reading.timestamp.second)

    if temperature >= 25:
        led.value(1)
        print("LED ON - Temperature is above or equal to 25°C")
    else:
        led.value(0)
        print("LED OFF - Temperature is below 25°C")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)   
wlan.connect(WIFI_NAME, WIFI_PASSWORD)

while not wlan.isconnected():
    print("Connecting to WiFi...")
    time.sleep(1)

print("Connected to WiFi. IP Address:", wlan.ifconfig()[0])

client = MQTTClient("subscriber", BROKER_IP, port = 8080)
client.set_callback(received_message)
client.connect()
client.subscribe(b"temp/pico")

print("Subscribed to topic: temp/pico")

while True:
    client.check_msg()  
    time.sleep(0.1)  

