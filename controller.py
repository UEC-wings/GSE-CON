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
    
class Controller(QMainWindow):
    
    status_flag = False # ON(TRUE)/OFF(FALSE) flag
    action_flag = ActionStatus.nothing
    
    def __init__(self):
        super(Controller, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.released_buttons()
        
    def released_buttons(self):
        self.ui.on_off_button.released.connect(self.released_on_off_button)
        # Radio buttons
        self.ui.fill_radio_button.released.connect(self.released_radio_button)
        self.ui.dump_radio_button.released.connect(self.released_radio_button)
        self.ui.ignition_radio_button.released.connect(self.released_radio_button)
        self.ui.purge_radio_button.released.connect(self.released_radio_button)
        
    def released_radio_button(self):
        sender = self.sender().text()
        if sender == "FILL":
            self.action_flag = ActionStatus.fill
        elif sender == "DUMP":
            self.action_flag = ActionStatus.dump
        elif sender == "IGNITION":
            self.action_flag = ActionStatus.ignition
        elif sender == "PURGE":
            self.action_flag = ActionStatus.purge
        else:
            self.action_flag = ActionStatus.nothing

    def released_on_off_button(self):
        print(self.action_flag)

    def status_on(self):
        self.status_flag = True
        self.ui.status_text.setText("ON")

    def status_off(self):
        self.status_flag = False
        self.ui.status_text.setText("OFF")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = Controller()
    MainWindow.show()
    app.exec()