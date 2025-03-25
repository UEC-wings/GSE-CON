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

# Valve state
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
    
    # Valve status
    status_n2o_fill = CLOSE
    status_n2o_dump = CLOSE
    status_o2_fill = CLOSE
    status_ignition = CLOSE
    
    # state of the buttons background color
    state_valve_open = 'background-color: red'
    state_valve_close = 'background-color: green'
    
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
        '''
        Initialize button signals.
        '''
        # valve control button connect signals
        self.ui.n2o_fill_button.released.connect(self.fill_button_released)
        self.ui.n2o_dump_button.released.connect(self.dump_button_released)
        self.ui.o2_fill_button.released.connect(self.purge_button_released)
        self.ui.ignition_button.released.connect(self.ignition_button_released)
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
        self.ui.n2o_fill_button.setDisabled(disable)
        self.ui.n2o_dump_button.setDisabled(disable)
        self.ui.o2_fill_button.setDisabled(disable)
        self.ui.ignition_button.setDisabled(disable)

    def show_socket_settings_dialog(self):
        settings_dialog = SocketSettingsDialog()
        # 他のwindowを触らせない
        settings_dialog.setModal(True)
        settings_dialog.exec()
    
    def connect_socket(self) -> None:
        if self.init_socket_client():
            # socketがopenしたとき、connectボタンを無効化し、他のボタンを有効化
            self.disable_buttons(False)
    
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
        n2o_fill: int = None,
        n2o_dump: int = None,
        o2_purge: int = None,
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
        # n2o_fill button status update
        if (n2o_fill is not None and n2o_fill == CLOSE):
            self.ui.fill_button.setStyleSheet(self.state_valve_close)
        elif (n2o_fill is not None and n2o_fill == OPEN):
            self.ui.fill_button.setStyleSheet('background-color: red')
        else:
            pass
        
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
