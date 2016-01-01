from socket import *
import binascii
import tongue


class TcpClient:
    HOST = '127.0.0.1'
    PORT = 12345
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    def __init__(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.ADDR)
        self.register_data = '7E0100002501860175250400020000000037' \
                             '303231385957333030302D42440000000000' \
                             '000000000000304A544931514B00A27E'
        self.packed_data = binascii.unhexlify(self.register_data)
        while True:
            self.client.send(self.packed_data)
            data = self.client.recv(self.BUFSIZ)
            if not data:
                break
            recv_data = tongue.Decode(data)
            print recv_data.dst


if __name__ == '__main__':
    client = TcpClient()
