import socket

def start_client():
    host = '127.0.0.1'  # Server address
    port = 12345        # Port to connect to

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server.")

    while True:
        message = input("You: ")
        client_socket.send(message.encode())  # Send message
        if not message:
            print("Connection closed.")
            break
        server_response = client_socket.recv(1024).decode()  # Receive response
        print(f"Server: {server_response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
