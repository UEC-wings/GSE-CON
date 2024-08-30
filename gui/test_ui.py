import sys
from PySide6.QtWidgets import *
import ui_ControlPanel
import ui_SensorMonitor
import ui_SocketSettingsDialog


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow1 = QMainWindow()
    MainWindow2 = QMainWindow()
    Dialog = QDialog()
    ui = ui_ControlPanel.Ui_ControlPanel()
    ui2 = ui_SensorMonitor.Ui_SensorMonitor()
    ui3 = ui_SocketSettingsDialog.Ui_SocketSettingsDialog()
    ui.setupUi(MainWindow1)
    ui2.setupUi(MainWindow2)
    ui3.setupUi(Dialog)
    MainWindow1.show()
    MainWindow2.show()
    Dialog.show()
    sys.exit(app.exec())