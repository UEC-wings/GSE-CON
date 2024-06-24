import socket
from typing import Optional

from PySide6.QtCore import *

class SocketClient(QObject):
    
    data_received_signal = Signal(bytes)
    
    def __init__(
            self,
            addr:str = 'localhost',
            port:int = 50000,
            family:int = socket.AF_INET,
            type:int = socket.SOCK_STREAM,
            timeout:int = 5,
            buffer:int = 32,
            blocking:bool=True
        ) -> None:
            '''socket通信clientクラス

            Args:
                address (int)   : ip address
                port (int)      : port
                family (int)    : address type ex(IPv4)) socket.AF_INET
                type (int)      : socket type ex(TCP)) socket.SOCK_STREAM
                timeout (int)   : timeout
                buffer (int)    : payload size
                blocking (bool) : Blocking or nonBlocking mode default)False nonblocking
            Memo:
                nonBlockingModeで実装
            '''
            super(SocketClient, self).__init__()
            self.server = (addr, port)
            self.family = family
            self.socket_type = type
            self.timeout = timeout
            self.buffer = buffer
            self._sock = socket.socket(
                self.family,
                self.socket_type
            )
            self._sock.settimeout(self.timeout)
            self._sock.setblocking(blocking)

    def connect_server(self):
        try:
            self._sock.connect(self.server)
        except Exception as e:
            print(e)
            return False
        else:
            return True
        
    def send(self, data) -> bool:
        try:
            self._sock.sendall(data)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def recv(self, buffer:int=0) -> Optional[bytes]:
        if buffer < 1:
            buffer = self.buffer
        try:
            data = self._sock.recv(buffer)
        except Exception as e:
            print(e)
            return None
        else:
            return data
        
    def received_data(self):
        while True:
            try:
                recv_data = self.recv()
                if recv_data:
                    self.data_received_signal.emit(recv_data)
                else:
                    self._sock.close()
                    break
            except Exception as e:
                print(e)
                self._sock.close()
                break

    def close(self):
        self._sock.shutdown(socket.SHUT_RDWR)
        self._sock.close()
