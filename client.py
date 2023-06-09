import socket
import logging


def send_data(server_address, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        msg = message + '\r\n'
        logging.warning(f"sending {msg}")
        sock.sendall(msg.encode('utf-8'))
        # Look for the response
        data = sock.recv(32)
        result = data.decode('utf-8')
        logging.warning(f"{result}")
    finally:
        logging.warning("closing")
        sock.close()


if __name__ == '__main__':
    server_address = ('172.16.16.101', 45000)
    message = 'TIME'
    send_data(server_address, message)
