import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.1.11" #running on the VM
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
client.publish("project/temp","Testing the publish method!!")#publish