import paho.mqtt.client as mqtt
import json
from group_10_util import print_data


def on_message(client, userdata, message):
    payload_str = message.payload.decode('utf-8')
    payload_dict = json.loads(payload_str)
    print("Received Message:")
    print_data(payload_dict)

def main():
    broker_address = "mqtt.eclipse.org"
    port = 1883
    topic = "iot_lab_topic"

    client = mqtt.Client("subscriber")
    client.on_message = on_message

    client.connect(broker_address, port)
    client.subscribe(topic)

    print(f"Subscribed to topic: {topic}")

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()

if __name__ == "__main__":
    main()