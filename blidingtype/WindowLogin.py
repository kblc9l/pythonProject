import sys
import PyQt5.QtWidgets as qtw
from work_with_db import login as lg
from blidingtype.windowlogin_ui import Ui_MainWindow

from blidingtype import WindowRegistration
import colors


def open_registration_window():
    ex1.close()
    ex2 = WindowRegistration.WindowRegistration()
    ex2.show()


class WindowLogin(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.form_layout = qtw.QFormLayout()
        self.ui.login_button.clicked.connect(self.data_validity_check)
        self.hide_error()
        self.ui.registration_edit.clicked.connect(self.go_to_registration)

    def go_to_registration(self):  # переход к окну регистрации
        pass

    def hide_error(self):  # скрыть блок ошибки
        self.ui.error_label.hide()
        self.ui.error.hide()
        self.ui.error_container.hide()

    def show_error(self):  # показать блок ошибки
        self.ui.error_label.show()
        self.ui.error.show()
        self.ui.error_container.show()

    def data_validity_check(self):  # проверка правильности ввода данных
        login = self.ui.login_edit.text()
        password = self.ui.password_edit.text()
        text_error = ''
        try:
            lg.check_login_in_db(login)
            lg.check_cor_password_in_db(login, password)
        except lg.NotLoginInDb:
            text_error = 'Пользователь не зарегитрирован'
            self.show_error()
        except lg.IncorrectPassword:
            text_error = 'Неверный пароль'
            self.show_error()

        if text_error == '':
            self.hide_error()
            pass  # открывание главного окна

        self.ui.error_label.setText(text_error)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    color = 'orange'
    style_file = colors.rewrite_qss('styles/login_style.qss', color)
    app.setStyleSheet(style_file)
    app.setStyleSheet(style_file)
    ex1 = WindowLogin()
    ex1.showMaximized()
    sys.exit(app.exec())
