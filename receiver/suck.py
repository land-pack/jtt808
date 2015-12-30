import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the part
server_address = ('192.168.0.76', 8888)
print >> sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Calling listen() puts the socket into server mode,
# and accept() waits for an incoming connection
flag = 1
# Listen for incoming connection
sock.listen(1)



while True:
    # Wait for a connection
    print >> sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >> sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if data:
                print data

            else:
                print >> sys.stderr, 'no more data from', client_address
                break
    finally:
        # clean up the connection
        connection.close()
