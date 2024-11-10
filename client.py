import socket

# config
server_ip = "127.0.0.1"  # replace with the server's IP address
server_port = 8001
msg = "send time"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

client.send(msg.encode("utf-8"))

response = client.recv(1024)
response = response.decode("utf-8")
   # if not response: break
print(response)
client.close()

