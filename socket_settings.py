from configparser import ConfigParser

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from gui.ui_SocketSettingsDialog import Ui_SocketSettingsDialog

class SocketSettingsDialog(QDialog):

    # socket settings ini file path
    _config_path        = './config/socket_settings.ini'
    # socket settings keys
    _section            = 'socket'
    _addr               = 'addr'
    _port               = 'port'
    _socket_type        = 'socket_type'
    _socket_family      = 'socket_family'
    _socket_timeout     = 'socket_timeout'
    _socket_buffer      = 'buffer_size'
    _socket_blocking    = 'blocking'
    
    def __init__(self):
        super(SocketSettingsDialog, self).__init__()
        self.ui = Ui_SocketSettingsDialog()
        self.ui.setupUi(self)
        self.init_settings()
    
    def init_settings(self):
        config = ConfigParser()
        config.read(self._config_path)
        self.set_addr(config[self._section][self._addr])
        self.set_port(config[self._section][self._port])
        self.set_socket_type(config[self._section][self._socket_type])
    
    def set_addr(self, addr: str):
        self.ui.addr_line_edit.setText(addr)
    
    def set_port(self, port: int):
        self.ui.port_line_edit.setText(port)
    
    def set_socket_type(self, socket_type: str):
        if socket_type == 'TCP':
            self.ui.socket_type_combo_box.setCurrentIndex(0)
        elif socket_type == 'UDP':
            self.ui.socket_type_combo_box.setCurrentIndex(1)
        else:
            raise ValueError('Invalid socket type')
        
if __name__ == '__main__':
    app = QApplication([])
    widget = SocketSettingsDialog()
    widget.show()
    app.exec()