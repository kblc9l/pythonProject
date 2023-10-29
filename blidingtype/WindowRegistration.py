import sqlite3
import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from checks import check_password, check_email, check_login
from work_with_db import registration
from blidingtype import WindowLogin




class WindowRegistration(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.form_layout = qtw.QFormLayout()
        self.setLayout(self.form_layout)

        self.label_1 = qtw.QLabel('Регистрация')
        self.label_1.setFont(qtg.QFont('Noto Sans', 20, 400))

        self.login_edit = qtw.QLineEdit(self)
        self.email_edit = qtw.QLineEdit(self)
        self.password_edit = qtw.QLineEdit(self)
        self.enter_button = qtw.QPushButton('Регистрация', clicked=lambda: self.data_validity_check())
        self.error_label = qtw.QLabel(self)

        self.form_layout.addRow('Введите логин:', self.login_edit)
        self.form_layout.addRow('Введите email:', self.email_edit)
        self.form_layout.addRow('Введите пароль:', self.password_edit)
        self.form_layout.addRow(self.enter_button)
        self.form_layout.addRow(self.error_label)

    def initUI(self):
        pass

    def data_validity_check(self):  # проверка правильности ввода данных
        login = self.login_edit.text()
        email = self.email_edit.text()
        password = self.password_edit.text()
        text_error = ''

        try:  # check password
            check_password.check_password(password)
        except check_password.LengthError:
            text_error = 'Пароль должен быть длинной не менее 8 символов'
        except check_password.LetterError:
            text_error = 'Пароль должен иметь буквы разного регистра'
        except check_password.DigitError:
            text_error = 'Пароль должен иметь цифры'
        except check_password.SequenceError:
            text_error = 'Пароль не должен содержать комбинации символов'
        except check_password.SpaceError:
            text_error = 'Пароль не должен содержать пробелов'

        try:  # check email
            check_email.check_email(email)
        except check_email.UnCorrectEmail:
            text_error = 'Email введён не корректно'
        except registration.EmailInDb:
            text_error = 'Этот email уже зарегистрирован'

        try:  # check login
            check_login.check_login(login)
        except check_login.LetterError:
            text_error = 'Логин должен состоять из символов a-z 0-9  . - _'
        except check_login.LenError:
            text_error = 'Длинна логина больше трёх символов'
        except registration.LoginInDb:
            text_error = 'Этот логин уже занят'

        self.error_label.setText(text_error)  # записываем ошибку в корректности данных, в так сказать, статус бар
        if self.error_label.text() == '':
            registration.entry_to_db(login, email, password)  # записываем данные в бд


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    ex1 = WindowRegistration()
    ex1.show()
    sys.exit(app.exec())
