import sys
import PyQt5.QtWidgets as qtw

import colors
from blidingtype.window_text_ui import Ui_Form


class WindowMain(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    color = 'orange'
    style_file = colors.rewrite_qss('styles/test_styles.qss', color)
    app.setStyleSheet(style_file)
    ex1 = WindowMain()
    ex1.showMaximized()
    sys.exit(app.exec())
