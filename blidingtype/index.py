import sys
import PyQt5.QtWidgets as qtw

import colors
from main_ui import Ui_MainWindow
from work_with_db import login as lg
from checks import check_password, check_email, check_login
from work_with_db import registration

flag = False


class WindowMain(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if not flag:
            self.go_to_preview()
        else:
            self.go_to_main()

    # function for switching window in main_container (QStacketWidget)

    def go_to_preview(self):
        self.ui.main_container.setCurrentIndex(0)
        self.ui.preview_registration_button.clicked.connect(self.go_to_registration)
        self.ui.preview_login_button.clicked.connect(self.go_to_login)

    def go_to_login(self):
        self.ui.main_container.setCurrentIndex(1)
        self.ui.login_login_button.clicked.connect(self.login_data_validity_check)
        self.login_hide_error()
        self.ui.login_registration_button.clicked.connect(self.go_to_registration)

    def go_to_registration(self):
        self.ui.main_container.setCurrentIndex(2)
        self.ui.registration_register_button.clicked.connect(self.registration_data_validity_check)
        self.registration_hide_error()
        self.ui.registration_login_button.clicked.connect(self.go_to_login)

    def go_to_main(self):
        self.ui.main_container.setCurrentIndex(3)

    # login ================================================================================

    def login_hide_error(self):
        self.ui.login_error_label.hide()
        self.ui.login_error.hide()
        self.ui.login_error_container.hide()

    def login_show_error(self):
        self.ui.login_error_label.show()
        self.ui.login_error.show()
        self.ui.login_error_container.show()

    def login_data_validity_check(self):
        login = self.ui.login_login_edit.text()
        password = self.ui.login_password_edit.text()
        text_error = ''
        try:
            lg.check_login_in_db(login)
            lg.check_cor_password_in_db(login, password)
        except lg.NotLoginInDb:
            text_error = 'Пользователь не зарегитрирован'
            self.login_show_error()
        except lg.IncorrectPassword:
            text_error = 'Неверный пароль'
            self.login_show_error()

        if text_error == '':
            self.login_hide_error()
            self.go_to_main()

        self.ui.login_error_label.setText(text_error)

    # registration ================================================================================

    def registration_hide_error(self):
        self.ui.registration_error_label.hide()
        self.ui.registration_error.hide()
        self.ui.registration_error_container.hide()

    def registration_show_error(self):
        self.ui.registration_error_label.show()
        self.ui.registration_error.show()
        self.ui.registration_error_container.show()

    def registration_data_validity_check(self):
        login = self.ui.registration_login_edit.text()
        email = self.ui.registration_email_edit.text()
        password = self.ui.registration_password_edit.text()
        text_error = ''

        try:  # check password
            check_password.check_password(password)
        except check_password.LengthError:
            text_error = 'Пароль должен быть длинной не менее 8 символов'
            self.registration_show_error()
        except check_password.LetterError:
            text_error = 'Пароль должен иметь буквы разного регистра'
            self.registration_show_error()
        except check_password.DigitError:
            text_error = 'Пароль должен иметь цифры'
            self.registration_show_error()
        except check_password.SequenceError:
            text_error = 'Пароль не должен содержать комбинации символов'
            self.registration_show_error()

        except check_password.SpaceError:
            text_error = 'Пароль не должен содержать пробелов'
            self.registration_show_error()

        try:  # check email
            check_email.check_email(email)
        except check_email.UnCorrectEmail:
            text_error = 'Email введён не корректно'
            self.registration_show_error()
        except registration.EmailInDb:
            text_error = 'Этот email уже зарегистрирован'
            self.registration_show_error()

        try:  # check login
            check_login.check_login(login)
        except check_login.LetterError:
            text_error = 'Логин должен состоять из символов a-z 0-9  . - _'
            self.registration_show_error()
        except check_login.LenError:
            text_error = 'Длинна логина больше трёх символов'
            self.registration_show_error()
        except registration.LoginInDb:
            text_error = 'Этот логин уже занят'
            self.registration_show_error()

        self.ui.registration_error_label.setText(text_error)
        if self.ui.registration_error_label.text() == '':
            self.registration_hide_error()
            registration.entry_to_db(login, email, password)
            self.go_to_login()
    # main ================================================================================


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    color = 'orange'

    style_file = colors.rewrite_qss('styles/style.qss', color)
    app.setStyleSheet(style_file)

    ex1 = WindowMain()
    ex1.showMaximized()

    sys.exit(app.exec())
