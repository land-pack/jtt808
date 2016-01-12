import asyncore
import socket
from core.dispatch import Dispatch
from visual.visual_decorator import info
from conf.settings import IP, PORT


class Adapt:
    def __init__(self, send_desc):
        self.sendall = send_desc  # For Adapt socket sendall() method


class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(8192)
        if data:
            conn = Adapt(self.send)  # Now your conn have method sendall()
            Dispatch(data, conn)


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
            info_tips = 'Incoming connection from %s' + repr(addr)
            info(info_tips)
            handler = EchoHandler(sock)


if __name__ == '__main__':
    server = EchoServer(IP, PORT)
    asyncore.loop()
