import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("UDP Server is listening on port 12345...")

try:
    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()

        print(f"Received from {addr}: {message}")

        # Check for exit command
        if message.lower() in ['exit', 'quit']:
            print("Exit command received. Shutting down server.")
            break

        # Echo the message back
        server_socket.sendto(data, addr)
        print(f"Echoed to {addr}: {message}")

finally:
    server_socket.close()
    print("Server socket closed.")
