# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
def send_to_server(text):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(text.encode('UTF-8'))
        data = s.recv(1024)

    print(f"Received {data!r}")
    return data.decode('UTF-8')