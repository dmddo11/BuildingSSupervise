import sys
import account
import logo
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QDialog, QDesktopWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MyApp(logo.iconMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Building Structure Supervise')

        logoLabel = logo.logoWidget().createLogo(80)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(logoLabel)

        loginButton = QPushButton('로그인')
        loginButton.clicked.connect(self.loginButtonClicked)
        signUpButton = QPushButton('회원가입')
        signUpButton.clicked.connect(self.signUpButtonClicked)

        accountLayout = QHBoxLayout()
        accountLayout.addWidget(loginButton)
        accountLayout.addWidget(signUpButton)

        mainLayout.addLayout(accountLayout)

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
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