import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.1.11" 
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Subscribing to topic","project/temp")
client.subscribe("project/temp")
print("Publishing message to topic","project/temp")
client.publish("project/temp","Testing the publish method!!")