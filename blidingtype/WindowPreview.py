import sys
import PyQt5.QtWidgets as qtw
from windowpreview_ui import Ui_MainWindow
from colors import COLOR


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
    with open('styles/preview.qss', 'r') as style_file:
        style_file = style_file.read()
        style_file = style_file.replace('background1000', COLOR[color]['background1000'])
        style_file = style_file.replace('background500', COLOR[color]['background500'])
        style_file = style_file.replace('background250', COLOR[color]['background250'])
        style_file = style_file.replace('background-dominant1', COLOR[color]['background-dominant1'])
        style_file = style_file.replace('background-dominant2', COLOR[color]['background-dominant2'])
        style_file = style_file.replace('warning', COLOR[color]['warning'])
        style_file = style_file.replace('background400', COLOR[color]['background400'])
    app.setStyleSheet(style_file)
    ex1 = WindowMain()
    ex1.showMaximized()

    sys.exit(app.exec())
