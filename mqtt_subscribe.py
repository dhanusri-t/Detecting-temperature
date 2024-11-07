import paho.mqtt.client as mqtt
import time
def on_message(client,userdata,message):
    print("Recieved message: ", str(message.payload.decode("utf-8")))
broker = "mqtt.eclipseprojects.io"
client = mqtt.Client(client_id="Smartphone", protocol=mqtt.MQTTv311)
client.connect(broker)
client.loop_start()
client.subscribe("Temperature/Home")
client.on_message = on_message
time.sleep(30)
client.loop_stop()

