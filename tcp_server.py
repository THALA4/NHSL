import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is listening on port 12345...")

conn, addr = server_socket.accept()
print(f"Connection established with {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Received data: {data.decode()}") # Convert bytes to string for display
    conn.sendall(data)  # Echo back the received data

conn.close()
server_socket.close()
print("Connection closed.")