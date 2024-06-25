from enum import Enum, auto

import numpy as np
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

from gui.ui_SensorMonitor import Ui_SensorMonitor
    
class SensorMonitor(QMainWindow):
    
    def __init__(self):
        super(SensorMonitor, self).__init__()
        self.ui = Ui_SensorMonitor()
        self.ui.setupUi(self)
        self.init_meter_view()
        self.sensor_timer = QtCore.QTimer()
        self.sensor_timer.timeout.connect(self.update)
        self.sensor_timer.start(50)
        self.datetime_widgets = QtCore.QTimer()
        self.datetime_widgets.timeout.connect(self.update_datetime)
        self.datetime_widgets.start(1000)
        
    def update_datetime(self):
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    def init_meter_view(self):
        # thrust meter
        self.ui.thrust_view.setTitle('Thrust Meter')
        self.ui.thrust_view.setLabel('left', 'Thrust', 'N')
        self.ui.thrust_view.setLabel('bottom', 'Time', 's')
        self.ui.thrust_view.setXRange(0, 100)
        self.ui.thrust_view.setYRange(0, 100)
        self.thrust_data = []
        self.thrust_curve = self.ui.thrust_view.plot(pen='r')
        # thremometer
        self.ui.thermo_view.setTitle('Temperature')
        self.ui.thermo_view.setLabel('left', 'Temperature', '℃')
        self.ui.thermo_view.setLabel('bottom', 'Time', 's')
        self.ui.thermo_view.setXRange(0, 100)
        self.ui.thermo_view.setYRange(0, 100)
        self.thermometer_data = []
        self.thermometer_curve = self.ui.thermo_view.plot(pen='r')


    def update(self):
        debug_data = np.random.randint(0, 100)
        # thrust
        self.thrust_data.append(debug_data)
        self.thrust_curve.setData(self.thrust_data)
        self.ui.thrust_view.setXRange(max(0, len(self.thrust_data) - 100), len(self.thrust_data))
        self.ui.thrust_label.setText(f"thrust: {debug_data} N")
        # thermometer
        self.thermometer_data.append(debug_data)
        self.thermometer_curve.setData(self.thermometer_data)
        self.ui.thermo_view.setXRange(max(0, len(self.thermometer_data) - 100), len(self.thermometer_data))
        self.ui.temp_label.setText(f"temp: {debug_data} ℃")
        
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = SensorMonitor()
    MainWindow.show()
    app.exec()