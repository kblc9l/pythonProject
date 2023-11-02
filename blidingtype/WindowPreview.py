import sys
import PyQt5.QtWidgets as qtw
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

    with open('styles/preview.qss', 'r') as style_file:
        style_file = style_file.read()
        style_file = style_file.replace('background1000', '#1b1b1b')
        style_file = style_file.replace('background500', '#292929')
        style_file = style_file.replace('background400', '#8080807a')
        style_file = style_file.replace('background250', '#808080')
        style_file = style_file.replace('background-dominant1', '#ffa31a')
        style_file = style_file.replace('background-dominant2', '#ffffff')
        style_file = style_file.replace('warning', '#c71700')

    app.setStyleSheet(style_file)
    ex1 = WindowMain()
    ex1.show()

    sys.exit(app.exec())
