
import paho.mqtt.client as mqtt
import json
from group_10_util import create_data
import time

def on_publish(client, userdata, mid):
    print(f"Message Published with MID: {mid}")

def publish_data(client, topic, payload):
    client.publish(topic, payload)

def main():
    broker_address = "mqtt.eclipse.org"
    port = 1883
    topic = "iot_lab_topic"

    client = mqtt.Client("publisher")
    client.connect(broker_address, port)

    for _ in range(10):
        payload = create_data()
        payload_str = json.dumps(payload)
        
        publish_data(client, topic, payload_str)
        print(f"Published: {payload_str}")

        time.sleep(1)

    client.disconnect()

if __name__ == "__main__":
    main()