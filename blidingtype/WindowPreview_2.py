import sys
import PyQt5.QtWidgets as qtw

import colors
from windowpreview_ui import Ui_MainWindow
from blidingtype import WindowLogin, WindowRegistration, WindowMain


class Appli(qtw.QApplication):
    class WindowMain(qtw.QMainWindow):
        def __init__(self):
            super().__init__()

            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.registration_button.clicked.connect(self.go_to_registration)
            self.ui.login_button.clicked.connect(self.go_to_login)

        def go_to_registration(self):
            pass
            # style_file_registration = colors.rewrite_qss('styles/registration_style.qss', color)
            # self.setStyleSheet(style_file_registration)
            # self.ex3 = WindowRegistration.WindowRegistration()
            # self.ex3.showMaximized()
            # self.hide()

        def go_to_login(self):
            self.ex1 = WindowRegistration.WindowRegistration()

    def __init__(self):
        super().__init__(sys.argv)
        color = 'orange'
        style_file = colors.rewrite_qss('styles/preview_style.qss', color)
        self.setStyleSheet(style_file)

        self.ex1 = self.WindowMain()
        self.ex1.showMaximized()

        sys.exit(self.exec())


if __name__ == '__main__':
    app = Appli()
