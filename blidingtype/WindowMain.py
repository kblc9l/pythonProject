import sys
import PyQt5.QtWidgets as qtw
from PyQt5 import QtGui
from windowlogin_ui import Ui_MainWindow


def enterButton(button):
    button.setFocus()


class WindowMain(qtw.QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_menu_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.focus = self.ui.test_lessons_div_2__text_button
        self.ui.test_lessons_div_2__text_button.setFocus()

        self.ui.test_lessons_div_1__text_button.clicked.connect(self.test_lessons_div_1__text_button_toggled)
        self.ui.test_lessons_div_1__text_button.enterEvent = lambda x: enterButton(
            self.ui.test_lessons_div_1__text_button)
        self.ui.test_lessons_div_1__text_button.leaveEvent = self.leaveButton

        self.ui.test_lessons_div_2__text_button.clicked.connect(self.test_lessons_div_2__text_button_toggled)
        self.ui.test_lessons_div_2__text_button.enterEvent = lambda x: enterButton(
            self.ui.test_lessons_div_2__text_button)
        self.ui.test_lessons_div_2__text_button.leaveEvent = self.leaveButton

        self.ui.test_lessons_div_2__lessons_button.clicked.connect(self.test_lessons_div_2__lessons_button_toggled)
        self.ui.test_lessons_div_2__lessons_button.enterEvent = lambda x: enterButton(
            self.ui.test_lessons_div_2__lessons_button)
        self.ui.test_lessons_div_2__lessons_button.leaveEvent = self.leaveButton

        self.ui.test_lessons_div_1__lessons_button.clicked.connect(self.test_lessons_div_1__lessons_button_toggled)
        self.ui.test_lessons_div_1__lessons_button.enterEvent = lambda x: enterButton(
            self.ui.test_lessons_div_1__lessons_button)
        self.ui.test_lessons_div_1__lessons_button.leaveEvent = self.leaveButton

        self.ui.color_setting_div_1__colors_button.clicked.connect(self.color_setting_div_1__colors_button_toggled)
        self.ui.color_setting_div_1__colors_button.enterEvent = lambda x: enterButton(
            self.ui.color_setting_div_1__colors_button)
        self.ui.color_setting_div_1__colors_button.leaveEvent = self.leaveButton

        self.ui.color_setting_div_2__color_button.clicked.connect(self.color_setting_div_2__color_button_toggled)
        self.ui.color_setting_div_2__color_button.enterEvent = lambda x: enterButton(
            self.ui.color_setting_div_2__color_button)
        self.ui.color_setting_div_2__color_button.leaveEvent = self.leaveButton

        self.ui.color_setting_div_1__settings_button.clicked.connect(self.color_setting_div_1__settings_button_toggled)
        self.ui.color_setting_div_1__settings_button.enterEvent = lambda x: enterButton(
            self.ui.color_setting_div_1__settings_button)
        self.ui.color_setting_div_1__settings_button.leaveEvent = self.leaveButton

        self.ui.color_setting_div_2__setting_button.clicked.connect(self.color_setting_div_2__setting_button_toggled)
        self.ui.color_setting_div_2__setting_button.enterEvent = lambda x: enterButton(
            self.ui.color_setting_div_2__setting_button)
        self.ui.color_setting_div_2__setting_button.leaveEvent = self.leaveButton

        self.ui.about_profile_div_1__about_button.clicked.connect(self.about_profile_div_1__about_button_toggled)
        self.ui.about_profile_div_1__about_button.enterEvent = lambda x: enterButton(
            self.ui.about_profile_div_1__about_button)
        self.ui.about_profile_div_1__about_button.leaveEvent = self.leaveButton

        self.ui.about_profile_div_2__about_button.clicked.connect(self.about_profile_div_2__about_button_toggled)
        self.ui.about_profile_div_2__about_button.enterEvent = lambda x: enterButton(
            self.ui.about_profile_div_2__about_button)
        self.ui.about_profile_div_2__about_button.leaveEvent = self.leaveButton

        self.ui.about_profile_div_1__profile_button.clicked.connect(self.about_profile_div_1__profile_button_toggled)
        self.ui.about_profile_div_1__profile_button.enterEvent = lambda x: enterButton(
            self.ui.about_profile_div_1__profile_button)
        self.ui.about_profile_div_1__profile_button.leaveEvent = self.leaveButton

        self.ui.about_profile_div_2__profile_button.clicked.connect(self.about_profile_div_2__profile_button_toggled)
        self.ui.about_profile_div_2__profile_button.enterEvent = lambda x: enterButton(
            self.ui.about_profile_div_2__profile_button)
        self.ui.about_profile_div_2__profile_button.leaveEvent = self.leaveButton

        self.ui.burger.enterEvent = self.enterForBurger
        self.ui.burger.leaveEvent = self.leaveForBurger
        self.ui.burger.clicked.connect(self.leaveButton)

        self.ui.reset_language.enterEvent = self.enterForReset_language
        self.ui.reset_language.leaveEvent = self.leaveForReset_language
        self.ui.reset_language.clicked.connect(self.leaveButton)

    # function for change button's icon

    def enterForBurger(self, event):
        self.ui.burger.setIcon(QtGui.QIcon('images/svg_icon/menu_orange.svg'))

    def leaveForBurger(self, event):
        self.ui.burger.setIcon(QtGui.QIcon('images/svg_icon/menu.svg'))

    def enterForReset_language(self, event):
        self.ui.reset_language.setIcon(QtGui.QIcon('images/svg_icon/globe_orange.svg'))

    def leaveForReset_language(self, event):
        self.ui.reset_language.setIcon(QtGui.QIcon('images/svg_icon/globe.svg'))

    def leaveButton(self, event):
        if self.ui.icon_menu_widget.isHidden():
            if self.ui.stackedWidget.currentWidget().objectName() == 'test':
                self.ui.test_lessons_div_2__text_button.setFocus()
            elif self.ui.stackedWidget.currentWidget().objectName() == 'lessons':
                self.ui.test_lessons_div_2__lessons_button.setFocus()
            elif self.ui.stackedWidget.currentWidget().objectName() == 'colors':
                self.ui.color_setting_div_2__color_button.setFocus()
            elif self.ui.stackedWidget.currentWidget().objectName() == 'setting':
                self.ui.color_setting_div_2__setting_button.setFocus()
            elif self.ui.stackedWidget.currentWidget().objectName() == 'about':
                self.ui.about_profile_div_2__about_button.setFocus()
            elif self.ui.stackedWidget.currentWidget().objectName() == 'profile':
                self.ui.about_profile_div_2__profile_button.setFocus()
        elif self.ui.full_menu_widget.isHidden():
            if self.ui.stackedWidget.currentWidget().objectName() == 'test':
                self.ui.test_lessons_div_1__text_button.setFocus()
            elif self.ui.stackedWidget.currentWidget().objectName() == 'lessons':
                self.ui.test_lessons_div_1__lessons_button.setFocus()
            elif self.ui.stackedWidget.currentWidget().objectName() == 'colors':
                self.ui.color_setting_div_1__colors_button.setFocus()
            elif self.ui.stackedWidget.currentWidget().objectName() == 'setting':
                self.ui.color_setting_div_1__settings_button.setFocus()
            elif self.ui.stackedWidget.currentWidget().objectName() == 'about':
                self.ui.about_profile_div_1__about_button.setFocus()
            elif self.ui.stackedWidget.currentWidget().objectName() == 'profile':
                self.ui.about_profile_div_1__profile_button.setFocus()

    #  function for changing menu page
    def test_lessons_div_1__text_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(0)
        self.focus = self.ui.test_lessons_div_1__text_button

    def test_lessons_div_2__text_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(0)
        self.focus = self.ui.test_lessons_div_2__text_button

    def test_lessons_div_2__lessons_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(1)
        self.focus = self.ui.test_lessons_div_2__lessons_button

    def test_lessons_div_1__lessons_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(1)
        self.focus = self.ui.test_lessons_div_1__lessons_button

    def color_setting_div_1__colors_button_toggled(self):
        pass

    def color_setting_div_2__color_button_toggled(self):
        pass

    def color_setting_div_1__settings_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(3)
        self.focus = self.ui.color_setting_div_1__settings_button

    def color_setting_div_2__setting_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(3)
        self.focus = self.ui.color_setting_div_2__setting_button

    def about_profile_div_1__about_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(4)
        self.focus = self.ui.about_profile_div_1__about_button

    def about_profile_div_2__about_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(4)
        self.focus = self.ui.about_profile_div_2__about_button

    def about_profile_div_1__profile_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(5)
        self.focus = self.ui.about_profile_div_1__profile_button

    def about_profile_div_2__profile_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(5)
        self.focus = self.ui.about_profile_div_2__profile_button


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    with open('styles/main_style.qss', 'r') as style_file:
        style_file = style_file.read()
        style_file = style_file.replace('background1000', '#1b1b1b')
        style_file = style_file.replace('background500', '#292929')
        style_file = style_file.replace('background250', '#808080')
        style_file = style_file.replace('background-dominant1', '#ffa31a')
        style_file = style_file.replace('background-dominant2', '#ffffff')
        style_file = style_file.replace('warning', '#c71700')

    app.setStyleSheet(style_file)
    ex1 = WindowMain()
    ex1.show()

    sys.exit(app.exec())
