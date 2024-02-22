import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65429  # The port used by the server

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, server")  # Send message to the server
        data = s.recv(1024)  # Receive response from the server
        print(f"Received {data.decode()!r}")
except ConnectionRefusedError:
    print("Connection was refused. Is the server running?")
except Exception as e:
    print(f"An error occurred: {e}")
