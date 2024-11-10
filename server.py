import socket
import datetime

# Config

server_ip = "127.0.0.1" # localhost
port = 8001
current_time = datetime.datetime.now()
response = "Aktuelles Dateum und Zeit: " + str(current_time)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, port))
server.listen(0)
print("Server now listening on port " + str(port))

(client_socket, client_address) = server.accept()
print("Accepted Connection from" + str(client_address))

while True:                                 # forever
    request = client_socket.recv(1024)    # receive data from client
    request = request.decode("utf-8")
    print("Request from Client: " + str(request))
    if not request: break                        # stop if client stopped
    client_socket.send(response.encode("utf-8"))
client_socket.close()
print("Server closed")
server.close()

