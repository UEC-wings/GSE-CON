from configparser import ConfigParser
from enum import Enum, auto

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from lib.socket_client import SocketClient

from socket_settings import SocketSettingsDialog
from gui.ui_ControlPanel import Ui_ControlPanel



OFF = 0
RELEASED = 1
ON = 2

class cmd(Enum):
    fill            = b'\xFF\xFF\xFF\xF0'
    dump            = b'\xFF\xFF\xFF\xF1'
    purge           = b'\xFF\xFF\xFF\xF2'
    ignition        = b'\xFF\xFF\xFF\xF3'
    off             = b'\x00\x00\x00\x00'
    status          = b'\x00\x00\x00\x01'
    on              = b'\x00\x00\x00\x02'

class valve(Enum):
    fill        = auto()
    dump        = auto()
    purge       = auto()
    ignition    = auto()

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
    
    status = {
        valve.fill      : OFF,
        valve.dump      : OFF,
        valve.purge     : OFF,
        valve.ignition  : OFF
    }

    def __init__(self):
        super(ControlPanel, self).__init__()
        self.ui = Ui_ControlPanel()
        self.ui.setupUi(self)
        #self.init_socket_client()
        self.set_button_status(
            fill=OFF,
            dump=OFF,
            purge=OFF,
            ignition=OFF
        )
        self.init_button_signals()

    def init_button_signals(self):
        self.ui.fill_button.released.connect(self.fill_button_released)
        self.ui.dump_button.released.connect(self.dump_button_released)
        self.ui.purge_button.released.connect(self.purge_button_released)
        self.ui.ignition_button.released.connect(self.ignition_button_released)
        self.ui.action_socket_settings.triggered.connect(self.show_socket_settings_dialog)
        self.ui.action_connect.triggered.connect(self.connect_socket)
        self.ui.action_disconnect.triggered.connect(self.disconnect_socket)
        self.ui.action_about_qt.triggered.connect(QApplication.instance().aboutQt)
        # connectボタン以外を無効化
        self.is_button_disable(True)
        
    def is_button_disable(self, disable: bool):
        """
        Enable or disable buttons based on the given boolean value.

        Args:
            disable (bool): true to disable buttons, false to enable buttons.
        
        Note:
            connectボタンとほかのボタンは排他的に有効化する
        """
        self.ui.action_connect.setDisabled(not disable)
        self.ui.action_disconnect.setDisabled(disable)
        self.ui.fill_button.setDisabled(disable)
        self.ui.dump_button.setDisabled(disable)
        self.ui.purge_button.setDisabled(disable)
        self.ui.ignition_button.setDisabled(disable)
        

    # TODO: 開いたときにMainWindowを触らせないようにする
    def show_socket_settings_dialog(self):
        settings_dialog = SocketSettingsDialog()
        settings_dialog.exec()
    
    def connect_socket(self) -> None:
        if self.init_socket_client():
            # socketがopenしたとき、connectボタンを無効化し、他のボタンを有効化
            self.is_button_disable(False)
    
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
            self.client_thread = QThread()
            self.client = SocketClient(
                addr = config[self._section][self._addr],
                port = int(config[self._section][self._port])
            )
            self.client.connect_server()
            self.client.moveToThread(self.client_thread)
            self.client.data_received_signal.connect(self.data_received_slot)
            self.client_thread.started.connect(self.client.received_data)
            self.client_thread.start()
        except Exception as e:
            print(e)
            return False
        else:
            return True
    
    def get_valve_status(self) -> dict:
        return self.status
    
    def fill_button_released(self):
        previous_status = self.status[valve.fill]
        self.status[valve.fill] = RELEASED
        self.set_button_status(fill=RELEASED)
        if previous_status == OFF:
            self.client.send(cmd.fill.value+cmd.on.value)
        elif previous_status == ON:
            self.client.send(cmd.fill.value+cmd.off.value)
        else:
            pass

    def dump_button_released(self):
        previous_status = self.status[valve.dump]
        self.status[valve.dump] = RELEASED
        self.set_button_status(dump=RELEASED)
        if previous_status == OFF:
            self.client.send(cmd.dump.value+cmd.on.value)
        elif previous_status == ON:
            self.client.send(cmd.dump.value+cmd.off.value)
        else:
            pass

    def purge_button_released(self):
        previous_status = self.status[valve.purge]
        self.status[valve.purge] = RELEASED
        self.set_button_status(purge=RELEASED)
        if previous_status == OFF:
            self.client.send(cmd.purge.value+cmd.on.value)
        elif previous_status == ON:
            self.client.send(cmd.purge.value+cmd.off.value)
        else:
            pass

    def ignition_button_released(self):
        previous_status = self.status[valve.ignition]
        self.status[valve.ignition] = RELEASED
        self.set_button_status(ignition=RELEASED)
        if previous_status == OFF:
            self.client.send(cmd.ignition.value+cmd.on.value)
        elif previous_status == ON:
            self.client.send(cmd.ignition.value+cmd.off.value)
        else:
            pass
    
    def set_button_status(
        self,
        fill: int = None,
        dump: int = None,
        purge: int = None,
        ignition: int = None
    ) -> None:
        """
        Sets the status of the buttons on the control panel.

        Args:
            fill (int, optional): The status of the fill button. Defaults to None.
            dump (int, optional): The status of the dump button. Defaults to None.
            purge (int, optional): The status of the purge button. Defaults to None.
            ignition (int, optional): The status of the ignition button. Defaults to None.

        """
        # fill valve status update
        if (fill is not None and fill == OFF):
            self.ui.fill_button.setStyleSheet('background-color: green')
        if (fill is not None and fill == RELEASED):
            self.ui.fill_button.setStyleSheet('background-color: yellow')
        if (fill is not None and fill == ON):
            self.ui.fill_button.setStyleSheet('background-color: red')
        # dump valve status update
        if (dump is not None and dump == OFF):
            self.ui.dump_button.setStyleSheet('background-color: green')
        if (dump is not None and dump == RELEASED):
            self.ui.dump_button.setStyleSheet('background-color: yellow')
        if (dump is not None and dump == ON):
            self.ui.dump_button.setStyleSheet('background-color: red')
        # purge valve status update
        if (purge is not None and purge == OFF):
            self.ui.purge_button.setStyleSheet('background-color: green')
        if (purge is not None and purge == RELEASED):
            self.ui.purge_button.setStyleSheet('background-color: yellow')
        if (purge is not None and purge == ON):
            self.ui.purge_button.setStyleSheet('background-color: red')
        # ignition valve status update
        if (ignition is not None and ignition == OFF):
            self.ui.ignition_button.setStyleSheet('background-color: green')
        if (ignition is not None and ignition == RELEASED):
            self.ui.ignition_button.setStyleSheet('background-color: yellow')
        if (ignition is not None and ignition == ON):
            self.ui.ignition_button.setStyleSheet('background-color: red')
        
        
    def update_valve_status(self, valve: valve, state: int):
        if valve == valve.fill:
            if state == OFF:
                self.ui.fill_button.setStyleSheet('background-color: green')
                self.status[valve.fill] = OFF
            elif state == ON:
                self.ui.fill_button.setStyleSheet('background-color: red')
                self.status[valve.fill] = ON
            else:
                pass
        if valve == valve.dump:
            if state == OFF:
                self.ui.dump_button.setStyleSheet('background-color: green')
                self.status[valve.dump] = OFF
            elif state == ON:
                self.ui.dump_button.setStyleSheet('background-color: red')
                self.status[valve.dump] = ON
            else:
                pass
        if valve == valve.purge:
            if state == OFF:
                self.ui.purge_button.setStyleSheet('background-color: green')
                self.status[valve.purge] = OFF
            elif state == ON:
                self.ui.purge_button.setStyleSheet('background-color: red')
                self.status[valve.purge] = ON
            else:
                pass
        if valve == valve.ignition:
            if state == OFF:
                self.ui.ignition_button.setStyleSheet('background-color: green')
                self.status[valve.ignition] = OFF
            elif state == ON:
                self.ui.ignition_button.setStyleSheet('background-color: red')
                self.status[valve.ignition] = ON
            else:
                pass

    def decode_command(self, data: bytes):
        try:
            # valve種類のデコード
            if data[0:4] == cmd.fill.value:
                header = valve.fill
            elif data[0:4] == cmd.dump.value:
                header = valve.dump
            elif data[0:4] == cmd.purge.value:
                header = valve.purge
            elif data[0:4] == cmd.ignition.value:
                header = valve.ignition
            else:
                header = None
            # 状態のデコード
            if data[4:8] == cmd.on.value:
                state = ON
            elif data[4:8] == cmd.off.value:
                state = OFF
            else:
                state = None
        except Exception as e:
            print(e)
            return None, None
        return header, state

    def data_received_slot(self, data: bytes):
        print(data)
        header, state = self.decode_command(data)
        print(header, state)
        self.update_valve_status(header, state)

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
