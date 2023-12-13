import socket

class SocketHost:
    def __init__(
            self,
            host,
            port=50000,
            family=socket.AF_INET,
            socket_type=socket.SOCK_STREAM    
        ):
        self._host = host
        self._port = port
        self._sock = socket.socket(family, socket_type)
        self._sock.bind((self.host, self.port))

    def listen(self):
        self._sock.listen(1)
        print('Listening on {}:{}'.format(self.host, self.port))

    def accept(self):
        self._conn, self._addr = self._sock.accept()
        print('Connected by', self._addr)

    def send(self, data):
        self._conn.sendall(data)

    def recv(self, size):
        return self._conn.recv(size)

    def close(self):
        self._conn.close()
