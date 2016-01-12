import asyncore
import socket
from core.dispatch import Dispatch


class Adapt:
    def __init__(self, send, data):
        self.sendall = send
        self.data = data
        Dispatch(send, data)


class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(8192)
        if data:
            Adapt(self.send, data)


class EchoServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = EchoHandler(sock)


server = EchoServer('0.0.0.0', 5555)
asyncore.loop()
