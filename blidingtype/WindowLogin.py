import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5 import uic

from work_with_db import login as lg
from blidingtype import WindowRegistration


def open_registration_window():
    ex1.close()
    ex2 = WindowRegistration.WindowRegistration()
    ex2.show()


class WindowLogin(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        uic.loadUi('designs/login.ui', self)
        self.form_layout = qtw.QFormLayout()

    def initUI(self):
        pass

    def data_validity_check(self):  # проверка правильности ввода данных
        login = self.login_edit.text()
        password = self.password_edit.text()
        text_error = ''

        try:
            lg.check_login_in_db(login)
            lg.check_cor_password_in_db(login, password)
        except lg.NotLoginInDb:
            text_error = 'Пользователь не зарегитрирован'
        except lg.IncorrectPassword:
            text_error = 'Неверный пароль'
        if text_error == '':
            print('Вы вошли в аккаунт')
        self.error_label.setText(text_error)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    ex1 = WindowLogin()
    ex1.show()

    sys.exit(app.exec())
