import socket

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f'Server starting at {HOST}:{PORT}')

client_socket, addr = server_socket.accept()
print(f'Client connected: {addr}')
while True:
    data = client_socket.recv(1024).decode()
    if not data or data.lower() == "exit":
        break
    print(f'Client: {data}')
    response = input('Server answer: ')
    client_socket.sendall(response.encode())
client_socket.close()
server_socket.close()

