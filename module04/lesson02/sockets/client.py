import socket


def client():
    host = socket.gethostname()
    port = 5555

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input('--> ')

    while message.lower().strip() != 'end':

        client_socket.send(message.encode())# send message to server

        data = client_socket.recv(1024).decode()  # recieve message from server
        print(f'received message: {data}')
        message = input('--> ')

    client_socket.close()


if __name__ == '__main__':
    client()
