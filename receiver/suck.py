import socket
import sys
from visual.visual_decorator import info, warning

sys.path.append("..")
# from dispatch_sample import dispatch_sample
from core.dispatch import Dispatch
from conf.settings import IP_PORT

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the part
server_address = IP_PORT
# server_address = ('0.0.0.0', 9909)
info_self = 'starting up on %s port ' + str(server_address)
info(info_self)
sock.bind(server_address)

# Calling listen() puts the socket into server mode,
# and accept() waits for an incoming connection
# Listen for incoming connection
sock.listen(1)

while True:
    # Wait for a connection
    info('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        info_one = 'connection from ' + str(client_address)
        info(info_one)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if data:
                # dispatch_sample(data.strip('\n'), connection)
                Dispatch(data, connection)
                pass

            else:
                warn_one = 'no more data from %s' + str(client_address)
                warning(warn_one)
                break
    finally:
        # clean up the connection
        connection.close()
