import socket

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print('Connecting to server. Enter "exit" for quit')

while True:
    message = input("Client says: ")
    client_socket.sendall(message.encode())
    if message.lower() == 'exit':
        break
    response = client_socket.recv(1024).decode()
    print(f'Server answer: {response}')

client_socket.close()
