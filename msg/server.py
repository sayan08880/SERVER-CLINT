import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server started on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        message = conn.recv(1024).decode()  # Receive message
        if not message:
            print("Client disconnected.")
            break
        print(f"Client: {message}")
        server_response = input("You: ")
        conn.send(server_response.encode())  # Send response

    conn.close()

if __name__ == "__main__":
    start_server()
