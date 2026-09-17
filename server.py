import socket

HOST = "192.168.10.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server started on {HOST}:{PORT}")
print("Waiting for client...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    message = conn.recv(1024).decode()

    if not message or message.lower() == "exit":
        print("Client disconnected.")
        break

    print("Client:", message)

    reply = input("Server: ")
    conn.send(reply.encode())

    if reply.lower() == "exit":
        break

conn.close()
server_socket.close()