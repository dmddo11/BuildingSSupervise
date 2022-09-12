import sys
import mysql
import encryption
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout


class loginWidget(QWidget):

    def __init__(self):
        super().__init__()

    def loginShow(self):
        loginPushButton = QPushButton('로그인')
        loginPushButton.clicked.connect(self.login)
        loginLayout = self.loginInfo()
        loginLayout.addWidget(loginPushButton)
        self.setLayout(loginLayout)

    def loginInfo(self):

        self.idLineEdit = QLineEdit()
        self.idLineEdit.setPlaceholderText('아이디')

        self.passwordLineEdit = QLineEdit()
        self.passwordLineEdit.setPlaceholderText('비밀번호')
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        loginLayout = QVBoxLayout()
        loginLayout.addWidget(self.idLineEdit)
        loginLayout.addWidget(self.passwordLineEdit)            

        return loginLayout

    def login(self):
        userDB = mysql.userDB()
        dbPassword = userDB.getPassword(self.idLineEdit.text()).encode('utf-8')
        encrypt = encryption.hash(self.passwordLineEdit.text())
        print(encrypt.checkHash(dbPassword))



class signUpWidget(loginWidget):

    def __init__(self):
        super().__init__()
    
    def signUpShow(self):
        signUpPushButton = QPushButton('회원가입')
        signUpPushButton.clicked.connect(self.signUp)
        signUpLayout = self.signUpInfo()
        signUpLayout.addWidget(signUpPushButton)
        self.setLayout(signUpLayout)
    
    def signUpInfo(self):

        self.nameLineEdit = QLineEdit()
        self.nameLineEdit.setPlaceholderText('이름')

        self.emailLineEdit = QLineEdit()
        self.emailLineEdit.setPlaceholderText('이메일')
        
        signUpLayout = self.loginInfo()
        signUpLayout.insertWidget(0, self.nameLineEdit)
        signUpLayout.insertWidget(3, self.emailLineEdit)
        
        return signUpLayout
    
    def signUp(self):
        userDB = mysql.userDB()
        encrypt = encryption.hash(self.passwordLineEdit.text())
        password = encrypt.makeHash().decode('utf-8')
        userDB.insert(self.nameLineEdit.text(), self.idLineEdit.text(), password, self.emailLineEdit.text())

        

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = signUpWidget()
   sys.exit(app.exec_())