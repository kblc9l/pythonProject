import sys
import PyQt5.QtWidgets as qtw

import colors
from windowpreview_ui import Ui_MainWindow
from blidingtype import WindowLogin, WindowRegistration


class WindowMain(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ex3 = None
        self.ex2 = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.registration_button.clicked.connect(self.go_to_registration)
        self.ui.login_button.clicked.connect(self.go_to_login)

    def go_to_registration(self):
        # style_file_registration = colors.rewrite_qss('styles/registration_style.qss', color)
        # app.setStyleSheet(style_file_registration)
        self.ex3 = WindowRegistration.WindowRegistration()
        self.ex3.showMaximized()
        self.hide()

    def go_to_login(self):
        # style_file_login = colors.rewrite_qss('styles/login_style.qss', color)
        # app.setStyleSheet(style_file_login)
        self.ex2 = WindowLogin.WindowLogin()
        self.ex2.showMaximized()
        self.hide()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    color = 'orange'

    style_file = colors.rewrite_qss('styles/preview_style.qss', color)
    app.setStyleSheet(style_file)
    ex1 = WindowMain()
    ex1.showMaximized()

    sys.exit(app.exec())
