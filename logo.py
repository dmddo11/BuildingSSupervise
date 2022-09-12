from PyQt5.QtWidgets import QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap

class logoWidget(QWidget):

    def __init__(self):
        super().__init__()
    
    def createLogo(self, height: int):
        logoPixmap = QPixmap('./png/logo.png')
        logoPixmap = logoPixmap.scaledToHeight(height)

        logoLabel = QLabel()
        logoLabel.setPixmap(logoPixmap)

        return logoLabel


class iconMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('./png/symbol_logo.png'))