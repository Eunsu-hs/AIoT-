import time
import paho.mqtt.client as mqtt

broker_address="192.168.137.97"
client = mqtt.Client("ClientPub")
client.connect(broker_address)

count = 0
try:
    while True:
        count = count + 1
        client.publish("hello", str(count))
        print(count)
        time.sleep(1.0)
    
except KeyboardInterrupt:
    pass
