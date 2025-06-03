import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.connect(('localhost', 12345))
print("Connected to the server on port 12345...")

try:
    while True:
        message = input("You: ")
        if message.lower() in ['exit', 'quit']:
            print("Closing connection...")
            break

        clientSocket.sendall(message.encode())
        data, addr = clientSocket.recvfrom(1024)
        print(f"Server: {data.decode()}")

finally:
    clientSocket.close()
    print("Connection closed.")
