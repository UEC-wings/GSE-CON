from enum import Enum, auto

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from lib.socket_client import SocketClient

from gui.ui_controlDialog import Ui_control_dialog

SETTINGS_INI = "./config/controller_settings.ini"

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

class ControlPanel(QDialog):

    # default server address and port
    addr = "192.168.100.100"
    port = 5000
    
    status = {
        valve.fill : OFF,
        valve.dump : OFF,
        valve.purge : OFF,
        valve.ignition : OFF
    }

    def __init__(self):
        super(ControlPanel, self).__init__()
        self.ui = Ui_control_dialog()
        self.ui.setupUi(self)
        self.init_socket_client()
        self.set_button_status(
            fill=OFF,
            dump=OFF,
            purge=OFF,
            ignition=OFF
        )
        # init signal slots buttons
        self.ui.fill_button.clicked.connect(self.fill_button_clicked)
        self.ui.dump_button.clicked.connect(self.dump_button_clicked)
        self.ui.purge_button.clicked.connect(self.purge_button_clicked)
        self.ui.ignition_button.clicked.connect(self.ignition_button_clicked)

    def init_socket_client(self) -> bool:
        try:
            self.client_thread = QThread()
            self.client = SocketClient(
                addr = self.addr,
                port = self.port
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
    
    def fill_button_clicked(self):
        previous_status = self.status[valve.fill]
        self.status[valve.fill] = RELEASED
        self.set_button_status(fill=RELEASED)
        if previous_status == OFF:
            self.client.send(cmd.fill.value+cmd.on.value)
        elif previous_status == ON:
            self.client.send(cmd.fill.value+cmd.off.value)
        else:
            pass

    def dump_button_clicked(self):
        previous_status = self.status[valve.dump]
        self.status[valve.dump] = RELEASED
        self.set_button_status(dump=RELEASED)
        if previous_status == OFF:
            self.client.send(cmd.dump.value+cmd.on.value)
        elif previous_status == ON:
            self.client.send(cmd.dump.value+cmd.off.value)
        else:
            pass

    def purge_button_clicked(self):
        previous_status = self.status[valve.purge]
        self.status[valve.purge] = RELEASED
        self.set_button_status(purge=RELEASED)
        if previous_status == OFF:
            self.client.send(cmd.purge.value+cmd.on.value)
        elif previous_status == ON:
            self.client.send(cmd.purge.value+cmd.off.value)
        else:
            pass

    def ignition_button_clicked(self):
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

        Raises:
            ValueError: If an invalid value is provided for any of the button statuses.
        """
        if (fill is not None):
            if fill == OFF:
                self.ui.fill_button.setStyleSheet('background-color: green')
            elif fill == RELEASED:
                self.ui.fill_button.setStyleSheet('background-color: yellow')
            elif fill == ON:
                self.ui.fill_button.setStyleSheet('background-color: red')
            else:
                raise ValueError("Invalid value")
        if (dump is not None):
            if dump == OFF:
                self.ui.dump_button.setStyleSheet('background-color: green')
            elif dump == RELEASED:
                self.ui.dump_button.setStyleSheet('background-color: yellow')
            elif dump == ON:
                self.ui.dump_button.setStyleSheet('background-color: red')
            else:
                raise ValueError("Invalid value")
        if (purge is not None):
            if purge == OFF:
                self.ui.purge_button.setStyleSheet('background-color: green')
            elif purge == RELEASED:
                self.ui.purge_button.setStyleSheet('background-color: yellow')
            elif purge == ON:
                self.ui.purge_button.setStyleSheet('background-color: red')
            else:
                raise ValueError("Invalid value")
        if (ignition is not None):
            if ignition == OFF:
                self.ui.ignition_button.setStyleSheet('background-color: green')
            elif ignition == RELEASED:
                self.ui.ignition_button.setStyleSheet('background-color: yellow')
            elif ignition == ON:
                self.ui.ignition_button.setStyleSheet('background-color: red')
            else:
                raise ValueError("Invalid value")

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
    dialog = ControlPanel()
    dialog.show()
    sys.exit(app.exec())
