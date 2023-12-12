from PySide6.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Slot

from toggle import ToggleButton

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('toggle button sample')

        font = QFont()
        font.setPointSize(72)
        font.setBold(True)
                    
        self.on_off_label = QLabel('off')
        self.on_off_label.setFont(font)

        self.toggle_button = ToggleButton()
        self.toggle_button.clicked.connect(self.handle_clicked)
        
        mainFrame = QHBoxLayout()
        mainFrame.addWidget(self.on_off_label)
        mainFrame.addWidget(self.toggle_button)
        
        self.setLayout(mainFrame)

    @Slot(bool)
    def handle_clicked(self, on_off):
        match on_off:
            case True:
                self.on_off_label.setText('on')
            case False:
                self.on_off_label.setText('off')
 
if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()