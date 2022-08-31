import sys
import account
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QDialog, QDesktopWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Building Structure Supervise')
        self.setWindowIcon(QIcon('./PNG/simbollogo.png'))
        logoPNG = QPixmap('./PNG/logo.png')
        logoPNG = logoPNG.scaledToHeight(80)

        logoImg = QLabel()
        logoImg.setPixmap(logoPNG)

        logoBox = QVBoxLayout()
        logoBox.addWidget(logoImg)    

        loginButton = QPushButton('로그인')
        loginButton.clicked.connect(self.loginButtonClicked)
        signUpButton = QPushButton('회원가입')
        signUpButton.clicked.connect(self.signUpButtonClicked)

        accountLayout = QHBoxLayout()
        accountLayout.addWidget(loginButton)
        accountLayout.addWidget(signUpButton)

        logoBox.addLayout(accountLayout)

        centralWidget = QWidget()
        centralWidget.setLayout(logoBox)
        self.setCentralWidget(centralWidget)

        self.center()
        self.resize(200, 100)
        self.show()
    
    def loginButtonClicked(self):
        self.loginWidget = account.loginWidget()
        self.loginWidget.loginShow()
        self.loginWidget.show()
    
    def signUpButtonClicked(self):
        self.signUpWidget = account.signUpWidget()
        self.signUpWidget.signUpShow()
        self.signUpWidget.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
       

class MainUI(QDialog):
    def __init__(self):
        super().__init__()




if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())