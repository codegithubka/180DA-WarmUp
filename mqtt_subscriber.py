import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("ece180d/test", qos=1)

def on_message(client, userdata, msg):
    print(f"Received: '{msg.payload.decode()}' on topic '{msg.topic}'")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected successfully.")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect_async("test.mosquitto.org")
client.loop_start()

try:
    while True:
        pass  # Keeps the subscriber running
except KeyboardInterrupt:
    print("Disconnecting...")
    client.loop_stop()
    client.disconnect()

