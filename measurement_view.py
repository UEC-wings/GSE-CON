from enum import Enum, auto


import numpy as np
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

from gui.ui_mainwindow import Ui_MainWindow
    
class SensorMonitor(QMainWindow):

    
    def __init__(self):
        super(SensorMonitor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_meter_view()
        # センサーの更新タイマー
        self.sensor_timer = QtCore.QTimer()
        self.sensor_timer.timeout.connect(self.update)
        self.sensor_timer.start(50)

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
        
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = SensorMonitor()
    MainWindow.show()
    app.exec()