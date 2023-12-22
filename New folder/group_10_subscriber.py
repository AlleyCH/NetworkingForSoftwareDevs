import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
print(f'\n{message.topic} \n{message.payload.decode("utf-8")}\n')
client = mqtt.Client() #instantiates a client
client.on_message = on_message #wire-up the on_message handler
client.connect('localhost', 1883) #connects to the server
client.subscribe('COMP216') # topic to subscribe to
while True:
client.loop_forever()