import paho.mqtt.client as mqtt
import time
import msvcrt

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

# Get the current time
start_time = time.time()

try:
    while True:
        # Check if 's' is pressed
        if msvcrt.kbhit() and msvcrt.getch().decode() == 's':
            client.loop_stop()
            break
        elif msvcrt.kbhit() and msvcrt.getch().decode() == 'a':
            client.publish("mymqtt/test1", payload="a", qos=1)

        # Check if 30 seconds have passed
        if time.time() - start_time >= 30:
            # Publish a message
            client.publish("mymqtt/test1", payload="keep alive", qos=1)
            # Reset the start time
            start_time = time.time()
except KeyboardInterrupt:
    pass

# Disconnect the MQTT client
client.disconnect()

# Print a success message
print("Successfully disconnected from the MQTT broker.")
