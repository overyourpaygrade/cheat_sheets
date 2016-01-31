import socket

myServerSocket = socket.socket()

localHost = socket.gethostname()

localPort = 5555

myServerSocket.bind((localHost, localPort))

myServerSocket.listen(1)

print 'Python-Forensics ... Waiting for Connection Request'

conn, clientInfo = myServerSocket.accept()

print 'Connection Received From:', clientInfo

conn.send('Connection Confirmed: '+'IP: '+ clientInfo[0] + ' Port: ' + str(clientInfo[1]))
