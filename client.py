import socket

SERVER_IP = "192.168.10.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

print(f"Connected to server {SERVER_IP}:{PORT}")

while True:
    message = input("Client: ")
    client_socket.send(message.encode())

    if message.lower() == "exit":
        break

    reply = client_socket.recv(1024).decode()
    print("Server:", reply)

    if reply.lower() == "exit":
        break

client_socket.close()