import socket
import json

client = socket.socket()
client.connect(('localhost',  8443))
data = {"name":"Dmitriy","id":"1352319","call":"Month"}
data = json.dumps(data)
client.send(data.encode())
client.close()
