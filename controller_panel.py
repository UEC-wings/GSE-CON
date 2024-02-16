from enum import Enum, auto

#from PySide6.QtCore import *
#from PySide6.QtWidgets import *
#from PySide6.QtGui import *

import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

from ui_mainwindow import Ui_MainWindow

class ActionStatus(Enum):
    nothing = auto()
    fill = auto()
    dump = auto()
    ignition = auto()
    purge = auto()
    
class ControllerPanel(QMainWindow):
    
    # ON(TRUE)/OFF(FALSE)
    action_flag = ActionStatus.nothing
    valve_status = {
        ActionStatus.fill       : False,
        ActionStatus.dump       : False,
        ActionStatus.ignition   : False,
        ActionStatus.purge      : False
    }
    
    def __init__(self):
        super(ControllerPanel, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_meter_view()
        self.released_buttons()
        # buttons background-color
        self.ui.on_off_button.setStyleSheet("QPushButton { background-color: green; }")
        self.ui.fill_radio_button.setStyleSheet("QRadioButton { background-color: white; }")
        self.ui.dump_radio_button.setStyleSheet("QRadioButton { background-color: white; }")
        self.ui.ignition_radio_button.setStyleSheet("QRadioButton { background-color: white; }")
        self.ui.purge_radio_button.setStyleSheet("QRadioButton { background-color: white; }")
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(50)
        
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
        if self.valve_status.get(self.action_flag):
            self.status_on()
        else:
            self.status_off()

    def released_on_off_button(self):
        if self.valve_status.get(self.action_flag):
            self.status_off()
        else:
            self.status_on()

    def status_on(self):
        self.ui.on_off_button.setText("OFF")
        self.ui.on_off_button.setStyleSheet("QPushButton { background-color: red; }")
        self.valve_status[self.action_flag] = True
        print(self.valve_status.values())
        
    def status_off(self):
        self.ui.on_off_button.setText("ON")
        self.ui.on_off_button.setStyleSheet("QPushButton { background-color: green; }")
        self.valve_status[self.action_flag] = False
        print(self.valve_status.values())

    def init_meter_view(self):
        # thrust meter
        self.ui.thrust_meter_view.setTitle('Thrust Meter')
        self.ui.thrust_meter_view.setLabel('left', 'Thrust', 'N')
        self.ui.thrust_meter_view.setLabel('bottom', 'Time', 's')
        self.ui.thrust_meter_view.setXRange(0, 100)
        self.ui.thrust_meter_view.setYRange(0, 100)
        self.thrust_data = []
        self.thrust_curve = self.ui.thrust_meter_view.plot(pen='r')
        # thremometer
        self.ui.thermometer_view.setTitle('Temperature')
        self.ui.thermometer_view.setLabel('left', 'Temperature', '℃')
        self.ui.thermometer_view.setLabel('bottom', 'Time', 's')
        self.ui.thermometer_view.setXRange(0, 100)
        self.ui.thermometer_view.setYRange(0, 100)
        self.thermometer_data = []
        self.thermometer_curve = self.ui.thermometer_view.plot(pen='r')


    def update(self):
        debug_data = np.random.randint(0, 100)
        # thrust
        self.thrust_data.append(debug_data)
        self.thrust_curve.setData(self.thrust_data)
        self.ui.thrust_meter_view.setXRange(max(0, len(self.thrust_data) - 100), len(self.thrust_data))
        self.ui.thrust_label.setText(f"thrust: {debug_data} N")
        # thermometer
        self.thermometer_data.append(debug_data)
        self.thermometer_curve.setData(self.thermometer_data)
        self.ui.thermometer_view.setXRange(max(0, len(self.thermometer_data) - 100), len(self.thermometer_data))
        self.ui.temp_label.setText(f"temp: {debug_data} ℃")
        if self.valve_status.get(ActionStatus.fill):
            self.ui.fill_label.setStyleSheet("QLabel { background-color: red; }")
        else:
            self.ui.fill_label.setStyleSheet("QLabel { background-color: green; }")
        if self.valve_status.get(ActionStatus.dump):
            self.ui.dump_label.setStyleSheet("QLabel { background-color: red; }")
        else:
            self.ui.dump_label.setStyleSheet("QLabel { background-color: green; }")
        if self.valve_status.get(ActionStatus.ignition):
            self.ui.ignition_label.setStyleSheet("QLabel { background-color: red; }")
        else:
            self.ui.ignition_label.setStyleSheet("QLabel { background-color: green; }")
        if self.valve_status.get(ActionStatus.purge):
            self.ui.purge_label.setStyleSheet("QLabel { background-color: red; }")
        else:
            self.ui.purge_label.setStyleSheet("QLabel { background-color: green; }")
            

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = ControllerPanel()
    MainWindow.show()
    app.exec()