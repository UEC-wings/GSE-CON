from enum import Enum, auto

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from gui.ui_mainwindow import Ui_MainWindow

class ActionStatus(Enum):
    nothing = auto()
    fill = auto()
    dump = auto()
    ignition = auto()
    purge = auto()
    
class ValveController(QMainWindow):
    
    # ON(TRUE)/OFF(FALSE)
    action_flag = ActionStatus.nothing
    valve_status = {
        ActionStatus.fill       : False,
        ActionStatus.dump       : False,
        ActionStatus.ignition   : False,
        ActionStatus.purge      : False
    }
    
    def __init__(self):
        super(ValveController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.released_buttons()
        # buttons background-color
        self.ui.on_off_button.setStyleSheet("QPushButton { background-color: green; }")
        self.ui.fill_radio_button.setStyleSheet("QRadioButton { background-color: white; }")
        self.ui.dump_radio_button.setStyleSheet("QRadioButton { background-color: white; }")
        self.ui.ignition_radio_button.setStyleSheet("QRadioButton { background-color: white; }")
        self.ui.purge_radio_button.setStyleSheet("QRadioButton { background-color: white; }")
        
    def released_buttons(self):
        self.ui.on_off_button.released.connect(self.released_on_off_button)
        # Radio buttons
        self.ui.fill_radio_button.released.connect(self.released_radio_button)
        self.ui.dump_radio_button.released.connect(self.released_radio_button)
        self.ui.ignition_radio_button.released.connect(self.released_radio_button)
        self.ui.purge_radio_button.released.connect(self.released_radio_button)
        
    def released_radio_button(self):
        sender = self.sender().text()
        self.ui.fill_radio_button.setStyleSheet("QRadioButton { background-color: white; }")
        self.ui.dump_radio_button.setStyleSheet("QRadioButton { background-color: white; }")
        self.ui.ignition_radio_button.setStyleSheet("QRadioButton { background-color: white; }")
        self.ui.purge_radio_button.setStyleSheet("QRadioButton { background-color: white; }")
        if sender == "FILL":
            self.action_flag = ActionStatus.fill
            self.ui.fill_radio_button.setStyleSheet("QRadioButton { background-color: yellow; }")
        elif sender == "DUMP":
            self.action_flag = ActionStatus.dump
            self.ui.dump_radio_button.setStyleSheet("QRadioButton { background-color: yellow; }")
        elif sender == "IGNITION":
            self.action_flag = ActionStatus.ignition
            self.ui.ignition_radio_button.setStyleSheet("QRadioButton { background-color: yellow; }")
        elif sender == "PURGE":
            self.action_flag = ActionStatus.purge
            self.ui.purge_radio_button.setStyleSheet("QRadioButton { background-color: yellow; }")
        else:
            self.action_flag = ActionStatus.nothing

    def released_on_off_button(self):
        if self.valve_status[self.action_flag]:
            self.status_off()
        else:
            self.status_on()

    def status_on(self):
        self.status_flag = True
        self.ui.status_text.setText("ON")
        self.ui.on_off_button.setText("OFF")
        self.ui.on_off_button.setStyleSheet("QPushButton { background-color: red; }")
        self.valve_status[self.action_flag] = True
        
    def status_off(self):
        self.status_flag = False
        self.ui.status_text.setText("OFF")
        self.ui.on_off_button.setText("ON")
        self.ui.on_off_button.setStyleSheet("QPushButton { background-color: green; }")
        self.valve_status[self.action_flag] = False

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = ValveController()
    MainWindow.show()
    app.exec()