import sys
import PyQt5.QtWidgets as qtw

import colors
from windowpreview_ui import Ui_MainWindow


class WindowMain(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.registration_button.clicked.connect(self.go_to_registration)
        self.ui.login_button.clicked.connect(self.go_to_login)

    def go_to_registration(self):
        pass

    def go_to_login(self):
        pass


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    color = 'orange'

    style_file = colors.rewrite_qss('styles/preview_style.qss', color)
    app.setStyleSheet(style_file)
    app.setStyleSheet(style_file)
    ex1 = WindowMain()
    ex1.showMaximized()

    sys.exit(app.exec())
