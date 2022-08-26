import sys
import pymysql
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
        if (self.idLineEdit.text() == 'admin' and self.passwordLineEdit.text() == 'admin'):
            print('login success!')
        else:
            print('login failed!')


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
        con = pymysql.connect(host='localhost', user='root', password='qwerasdf12', db='bss', charset='utf8')
        cur = con.cursor()
        sql = "select * from user"
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)
        con.close()

        

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = signUpWidget()
   sys.exit(app.exec_())