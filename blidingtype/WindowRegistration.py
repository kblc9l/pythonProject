import sys
import PyQt5.QtWidgets as qtw
from checks import check_password, check_email, check_login
from work_with_db import registration
from blidingtype.windowregister_ui import Ui_MainWindow
import colors


class WindowRegistration(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.register_button.clicked.connect(self.data_validity_check)
        self.hide_error()

    def hide_error(self): # скрыть блок ошибки
        self.ui.error_label.hide()
        self.ui.error.hide()
        self.ui.error_container.hide()

    def show_error(self):   # показать блок ошибки
        self.ui.error_label.show()
        self.ui.error.show()
        self.ui.error_container.show()

    def data_validity_check(self):  # проверка правильности ввода данных
        login = self.ui.login_edit.text()
        email = self.ui.email_edit.text()
        password = self.ui.password_edit.text()
        text_error = ''

        try:  # check password
            check_password.check_password(password)
        except check_password.LengthError:
            text_error = 'Пароль должен быть длинной не менее 8 символов'
            self.show_error()
        except check_password.LetterError:
            text_error = 'Пароль должен иметь буквы разного регистра'
            self.show_error()
        except check_password.DigitError:
            text_error = 'Пароль должен иметь цифры'
            self.show_error()
        except check_password.SequenceError:
            text_error = 'Пароль не должен содержать комбинации символов'
            self.show_error()

        except check_password.SpaceError:
            text_error = 'Пароль не должен содержать пробелов'
            self.show_error()

        try:  # check email
            check_email.check_email(email)
        except check_email.UnCorrectEmail:
            text_error = 'Email введён не корректно'
            self.show_error()
        except registration.EmailInDb:
            text_error = 'Этот email уже зарегистрирован'
            self.show_error()

        try:  # check login
            check_login.check_login(login)
        except check_login.LetterError:
            text_error = 'Логин должен состоять из символов a-z 0-9  . - _'
            self.show_error()
        except check_login.LenError:
            text_error = 'Длинна логина больше трёх символов'
            self.show_error()
        except registration.LoginInDb:
            text_error = 'Этот логин уже занят'
            self.show_error()

        self.ui.error_label.setText(text_error)  # записываем ошибку в корректности данных, в так сказать, статус бар
        if self.ui.error_label.text() == '':
            self.hide_error()
            registration.entry_to_db(login, email, password)  # записываем данные в бд


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    color = 'orange'
    style_file = colors.rewrite_qss('styles/registration_style.qss', color)
    app.setStyleSheet(style_file)
    ex1 = WindowRegistration()
    ex1.showMaximized()
    sys.exit(app.exec())
