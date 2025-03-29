from configparser import ConfigParser
from enum import Enum, auto

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from socket_client import SocketClient

from socket_settings import SocketSettingsDialog
from gui.ui_ControlPanel import Ui_ControlPanel


# Button state
OFF = 0
RELEASED = 1
ON = 2

# Valve&sock state
OPEN = 1
CLOSE = 0

class ControlPanel(QMainWindow):
    
    # socket settings ini file path
    _config_path        = './config/socket_settings.ini'
    #TODO: iniファイルのkeyを他のクラスでも書いているので、一箇所にまとめるか、getterを作るかする
    # socket settings keys
    _section            = 'socket'
    _addr               = 'addr'
    _port               = 'port'
    _socket_type        = 'socket_type'
    _socket_family      = 'socket_family'
    _socket_timeout     = 'socket_timeout'
    _socket_buffer      = 'buffer_size'
    _socket_blocking    = 'blocking'
    
    # send valve status
    status_send_n2o_fill = CLOSE
    status_send_n2o_dump = CLOSE
    status_send_o2_fill = CLOSE
    status_send_ignition = CLOSE
    
    # received valve status
    status_recv_n2o_fill = CLOSE
    status_recv_n2o_dump = CLOSE
    status_recv_o2_fill = CLOSE
    status_recv_ignition = CLOSE
    
    # state of the buttons background color
    state_open = 'background-color: green'
    state_close = 'background-color: red'
    
    def __init__(self):
        super(ControlPanel, self).__init__()
        self.ui = Ui_ControlPanel()
        self.ui.setupUi(self)
        #self.init_socket_client()
        self.init_button_signals()
        self.ui.current_connection_label.setText("Disconnected")
        self.ui.current_connection_label.setStyleSheet(self.state_close)

    def init_button_signals(self):
        '''
        Initialize button signals.
        '''
        # valve control button connect signals
        ## open&close functions
        ### n2o fill button 
        self.ui.open_n2o_fill_button.released.connect(self.open_n2o_fill_button_released)
        self.ui.close_n2o_fill_button.released.connect(self.close_n2o_fill_button_released)
        ### n2o dump button
        self.ui.open_n2o_dump_button.released.connect(self.open_n2o_dump_button_released)
        self.ui.close_n2o_dump_button.released.connect(self.close_n2o_dump_button_released)
        ### o2 fill button
        self.ui.open_o2_fill_button.released.connect(self.open_o2_fill_button_released)
        self.ui.close_o2_fill_button.released.connect(self.close_o2_fill_button_released)
        ### ignition button
        self.ui.on_ignition_button.released.connect(self.on_ignition_button_released)
        self.ui.off_ignition_button.released.connect(self.off_ignition_button_released)
        
        # socket setting actions connect signals
        self.ui.action_socket_settings.triggered.connect(self.show_socket_settings_dialog)
        self.ui.action_connect.triggered.connect(self.connect_socket)
        self.ui.action_disconnect.triggered.connect(self.disconnect_socket)
        # help actions connect signals
        self.ui.action_about_qt.triggered.connect(QApplication.instance().aboutQt)
        
    def disable_buttons(self, disable: bool):
        """
        Enable or disable buttons based on the given boolean value.

        Args:
            disable (bool): true to disable buttons, false to enable buttons.
        
        Note:
            connectボタンとほかのボタンは排他的に有効化する
        """
        self.ui.action_connect.setDisabled(not disable)
        self.ui.action_disconnect.setDisabled(disable)

# ---------------------------------------------------------------
# ------------------ Socket Settings dialog ---------------------
# ---------------------------------------------------------------
    def show_socket_settings_dialog(self):
        settings_dialog = SocketSettingsDialog()
        # 他のwindowを触らせない
        settings_dialog.setModal(True)
        settings_dialog.exec()

# ---------------------------------------------------------------
# ------------------ Socket Client functions --------------------
# ---------------------------------------------------------------
    def connect_socket(self) -> None:
        if self.init_socket_client():
            # socketがopenしたとき、connectボタンを無効化し、他のボタンを有効化
            self.disable_buttons(False)
            self.ui.current_connection_label.setText("Connected")
            self.ui.current_connection_label.setStyleSheet(self.state_open)
    
    def disconnect_socket(self) -> None:
        self.client.close()
        self.client_thread.quit()
        self.client_thread.wait()
        # socketがcloseしたとき、disconnectボタンを無効化し、connectボタンを有効化
        self.ui.action_connect.setDisabled(False)
        self.ui.action_disconnect.setDisabled(True)
    
    def init_socket_client(self) -> bool:
        config = ConfigParser()
        config.read(self._config_path)
        try:
            self.client = SocketClient(
                addr = config[self._section][self._addr],
                port = int(config[self._section][self._port])
            )
            if not self.client.connect_server():
                raise("Failed to connect to the server.")
        except Exception as e:
            self.show_alert_dialog(e)
            return False
        else:
            self.client_thread = QThread()
            self.client.moveToThread(self.client_thread)
            self.client.data_received_signal.connect(self.data_received_slot)
            self.client_thread.started.connect(self.client.received_data)
            self.client_thread.start()
            return True
    
    def send_data(self, data: bytes) -> bool:
        # packet format
        STX1 = 0x0F
        STX2 = 0xF0
        count = 0x01
        mode = 0x00 | data
        crc_hi = 0x11
        crc_lo = 0x11
        packet_send = bytearray([STX1, STX2, count, mode, crc_hi, crc_lo])
        try:
            self.client.send(packet_send)
        except Exception as e:
            self.show_alert_dialog(e)
            return False
        else:
            return True
    
    def data_received_slot(self, data: bytes):
        print(data)

# ---------------------------------------------------------------
# ------------------ Button Released functions ------------------
# ---------------------------------------------------------------
    def open_n2o_fill_button_released(self):
        self.status_send_n2o_fill = OPEN
        self.send_data(0x01)
    
    def close_n2o_fill_button_released(self):
        self.status_send_n2o_fill = CLOSE
        self.send_data(0x00)
        
    def open_n2o_dump_button_released(self):
        self.status_send_n2o_dump = OPEN
        self.send_data(0x03)
    
    def close_n2o_dump_button_released(self):
        self.status_send_n2o_dump = CLOSE
        self.send_data(0x02)
    
    def open_o2_fill_button_released(self):
        self.status_send_o2_fill = OPEN
        self.send_data(0x05)
    
    def close_o2_fill_button_released(self):
        self.status_send_o2_fill = CLOSE
        self.send_data(0x04)
    
    def on_ignition_button_released(self):
        self.status_send_ignition = ON
        self.send_data(0x07)
    
    def off_ignition_button_released(self):
        self.status_send_ignition = OFF
        self.send_data(0x06)

        
    def show_alert_dialog(self, msg: str):
        # QMessageBoxのインスタンスを作成
        warning_msg = QMessageBox()
        # 警告アイコンを設定
        warning_msg.setIcon(QMessageBox.Warning)
        # メッセージボックスのタイトルを設定
        warning_msg.setWindowTitle("Warning")
        # 表示するテキストを設定
        warning_msg.setText("An error occurred.")
        # 詳細メッセージを設定 (オプション)
        warning_msg.setInformativeText(f"{msg}")
        # メッセージボックスのボタンを設定
        warning_msg.setStandardButtons(QMessageBox.Ok)
        # デフォルトのボタンを設定 (オプション)
        warning_msg.setDefaultButton(QMessageBox.Ok)
        warning_msg.exec()

    def closeEvent(self, event):
        self.client.close()
        self.client_thread.quit()
        self.client_thread.wait()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = ControlPanel()
    MainWindow.show()
    sys.exit(app.exec())
