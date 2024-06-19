import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
import prg12

db = sqlite3.connect('dtbs.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT
)''')
db.commit()


class Registration(QMainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.ui = prg12.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setText('')
        self.ui.label_2.setText('Регистрация')
        self.ui.pbtn2.setText('Вход')
        self.ui.pbtn1.setText('Регистрация')
        self.setWindowTitle('Регистрация')

        self.ui.pbtn2.clicked.connect(self.login)
        self.ui.pbtn1.clicked.connect(self.reg)

    def login(self):
        self.loginWindow = Login()
        self.loginWindow.show()
        self.hide()

    def reg(self):
        user_login = self.ui.logini.text()
        user_password = self.ui.passwordi.text()

        if len(user_login) == 0 or len(user_password) == 0:
            return

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users VALUES ("{user_login}", "{user_password}")')
            self.ui.label.setText(f'Аккаунт {user_login} успешно зарегистрирован!')
            db.commit()
        else:
            self.ui.label.setText('Такая записать уже имеется!')


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = prg12.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setText('')
        self.ui.label_2.setText('Логин')
        self.ui.pbtn1.setText('Вход')
        self.ui.pbtn2.setText('Регистрация')
        self.setWindowTitle('Вход')

        self.ui.pbtn1.clicked.connect(self.login)
        self.ui.pbtn2.clicked.connect(self.reg)

    def reg(self):
        self.regWindow = Registration()
        self.regWindow.show()
        self.hide()

    def login(self):
        user_login = self.ui.logini.text()
        user_password = self.ui.passwordi.text()

        if len(user_login) == 0 or len(user_password) == 0:
            return

        cursor.execute(f'SELECT password FROM users WHERE login="{user_login}"')
        check_pass = cursor.fetchall()

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        check_login = cursor.fetchall()

        if check_pass and check_login and check_pass[0][0] == user_password and check_login[0][0] == user_login:
            self.ui.label.setText('Успешная авторизация!')
        else:
            self.ui.label.setText('Ошибка авторизации!')


if __name__ == '__main__':
    App = QApplication(sys.argv)
    loginWindow = Login()
    loginWindow.show()
    sys.exit(App.exec_())