import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttbroker = "mqtt.eclipseprojects.io"
client = mqtt.Client(client_id="Inside_Temperature", protocol=mqtt.MQTTv311)

client.connect(mqttbroker)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("Temperature/Home",randNumber)
    print("Just published " + str(randNumber) + "to Topic Temperature/Home")
    time.sleep(1)
    
    