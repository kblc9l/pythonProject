import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from checks import check_password, check_email, check_login


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
        self.enter_button = qtw.QPushButton('Регистрация', clicked=lambda: self.registration())
        self.error_label = qtw.QLabel(self)

        self.form_layout.addRow('Введите логин:', self.login_edit)
        self.form_layout.addRow('Введите email:', self.email_edit)
        self.form_layout.addRow('Введите пароль:', self.password_edit)
        self.form_layout.addRow(self.enter_button)
        self.form_layout.addRow(self.error_label)

    def initUI(self):
        pass

    def registration(self):
        login = self.login_edit.text()
        email = self.email_edit.text()
        password = self.password_edit.text()
        text_error = ''

        try:  # проверка пароля
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
        finally:
            self.error_label.setText(text_error)

        try:  # проверка email
            check_email.check_email(email)
        except check_email.UnCorrectEmail:
            self.error_label.setText('Email введён не корректно')

        try:  # проверка логина
            check_login.check_login(login)
        except check_login.LetterError:
            self.error_label.setText('Логин должен состоять из символов a-z 0-9  . - _')
        except check_login.LenError:
            self.error_label.setText('Длинна логина больше трёх символов')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    ex = WindowRegistration()
    ex.show()
    sys.exit(app.exec())
