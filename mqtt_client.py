import paho.mqtt.client as mqtt
import time

# Define the on_message callback function
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

# Create a MQTT client
client = mqtt.Client()

# Set the on_message callback function
client.on_message = on_message

# Connect to the broker
client.connect("broker.hivemq.com", 1883)

# Subscribe to the topic
client.subscribe("mymqtt/test2", qos=1)

# Start the loop
client.loop_start()

try:
    while True:
        # Publish a message every 5 seconds
        client.publish("mymqtt/test1", payload="hello", qos=1)
        time.sleep(5)
except KeyboardInterrupt:
    # Disconnect the MQTT client
    client.disconnect()

    # Print a success message
    print("Successfully disconnected from the MQTT broker.")
