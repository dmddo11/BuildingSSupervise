import sys
import account
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QDialog


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')

        loginButton = QPushButton('로그인')
        loginButton.clicked.connect(self.loginButtonClicked)
        signUpButton = QPushButton('회원가입')
        signUpButton.clicked.connect(self.signUpButtonClicked)

        accountLayout = QHBoxLayout()
        accountLayout.addWidget(loginButton)
        accountLayout.addWidget(signUpButton)

        centralWidget = QWidget()
        centralWidget.setLayout(accountLayout)
        self.setCentralWidget(centralWidget)

        self.move(300, 300)
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

class MainUI(QDialog):
    def __init__(self):
        super().__init__()




if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())