import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_message = on_message

broker_address="192.168.137.97"
client.connect(broker_address)
client.subscribe("pc",1)

client.loop_forever()