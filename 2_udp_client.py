import time
import math
import socket
import json

# Set up the server address and port to connect to
server_address = '127.0.0.1'
server_port = 8000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        # Send data
        message = {
            "x": 2 * math.sin(time.time()),
            "y": 2 * math.cos(time.time()),
            }

        buffer = json.dumps(message)
        print(f"send: {message}")
        sent = sock.sendto(buffer.encode(), (server_address, server_port))

        # Receive response
        data, server = sock.recvfrom(4096)
        print(f"recv: {data.decode()}")

except KeyboardInterrupt:
    sock.close()

