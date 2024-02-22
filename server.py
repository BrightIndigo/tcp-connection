import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65429  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        # Send initial message to the client
        message = "mess from server"
        conn.sendall(message.encode())

        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
        except (ConnectionResetError, ConnectionAbortedError):
            print("Client closed the connection unexpectedly.")
