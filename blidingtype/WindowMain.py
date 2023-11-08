import random
import sys

import PyQt5.QtWidgets as qtw

from PyQt5 import QtGui
from PyQt5.QtCore import QSize, QTimer

from blidingtype.window_main_ui_2 import Ui_MainWindow
import colors

STRING = ''
MODE = 'time'
OLL_COUNT_LETTER = 0
RIGHT_COUNT_LETTER = 0
COUNT_WORDS = 0


class LineEdit(qtw.QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.isActive)

        self.count_second = 0
        self.interval_time = 60
        self.write = True

    code_key = [192, 49, 50, 51, 52, 53, 54, 55, 56, 57, 48, 189, 187, 220, 221, 219, 80, 79, 73, 85, 89, 84, 82, 69,
                87, 81, 65, 83, 68, 70, 71, 72, 74, 75, 76, 186, 222, 191, 190, 188, 77, 78, 66, 86, 67, 88, 90, 32]

    def isActive(self):
        self.count_second += 1
        if self.count_second == self.interval_time:  # кол-во секунд
            self.timer.stop()
            self.write = False
            self.count_second = 0
            print('таймер остановился')

            show_result(COUNT_WORDS, RIGHT_COUNT_LETTER, RIGHT_COUNT_LETTER / OLL_COUNT_LETTER)
            # функция для окрываний ряздела статистики по тесту

    def keyPressEvent(self, e):
        self.setStyleSheet("""border: 1px solid rgba(0, 0, 0, 0);""")

        global STRING, OLL_COUNT_LETTER, RIGHT_COUNT_LETTER, COUNT_WORDS

        t, k = e.text(), e.nativeVirtualKey()

        if k in self.code_key and self.write:
            if OLL_COUNT_LETTER == 0:
                self.timer.start()
                print('таймер запустился')
            if STRING:
                OLL_COUNT_LETTER += 1  # увеличение общего кол-ва символов
                if t == STRING[0]:
                    if t == ' ':
                        COUNT_WORDS += 1  # увеличиваем количество слов
                    super().keyPressEvent(e)
                    STRING = STRING[1:]
                    RIGHT_COUNT_LETTER += 1  # увеличение кол-ва правильных символов
                else:
                    wrong_letter(LINEEDIT)  # выводим ошибку
            else:
                WindowMain.generate_text_for_test(ex1)  # генерируем новую строку, когда ввели всю строку


LINEEDIT: LineEdit


def show_result(words, right, percent):  # отображаем результаты в другом разделе
    print(words, right, round(percent, 2) * 100)  # статистика
    ex1.show_result(words, right, percent)


def wrong_letter(line):  # изменяем цвет обводки, для отображения ошибки
    line.setStyleSheet("""border: 1px solid #c71700;""")


def generate_string():
    global STRING, OLL_COUNT_LETTER, RIGHT_COUNT_LETTER
    with open('data/easy_words.txt', 'r', encoding='utf8') as f:
        f = f.read().split()
        s = ''
        while len(s) <= 55:
            s += random.choice(f) + ' '
        s = s[:s.rfind(' ')]
    STRING = s


generate_string()


def enter_button(button):
    button.setFocus()


class WindowMain(qtw.QMainWindow):
    global STRING

    def __init__(self):
        global LINEEDIT
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_menu_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.focus = self.ui.test_lessons_div_2__text_button
        self.ui.test_lessons_div_2__text_button.setFocus()

        self.input_text = LineEdit(self.ui.container_typed_text)
        self.input_text.setMinimumSize(QSize(0, 180))
        self.input_text.setObjectName("input_text")
        self.ui.verticalLayout_13.addWidget(self.input_text)
        self.input_text.setFocus()

        self.ui.given_text.setText(STRING)
        LINEEDIT = self.input_text

        self.initUi()

    def initUi(self):
        self.ui.refrech_button.clicked.connect(self.generate_text_for_test_result)
        self.ui.next_test_button.clicked.connect(self.generate_text_for_test_result)
        self.ui.refrech_button_2.setEnabled(False)

        self.ui.test_lessons_div_1__text_button.clicked.connect(self.test_lessons_div_1__text_button_toggled)
        self.ui.test_lessons_div_1__text_button.enterEvent = lambda x: enter_button(
            self.ui.test_lessons_div_1__text_button)
        self.ui.test_lessons_div_1__text_button.leaveEvent = self.leave_button

        self.ui.test_lessons_div_2__text_button.clicked.connect(self.test_lessons_div_2__text_button_toggled)
        self.ui.test_lessons_div_2__text_button.enterEvent = lambda x: enter_button(
            self.ui.test_lessons_div_2__text_button)
        self.ui.test_lessons_div_2__text_button.leaveEvent = self.leave_button

        self.ui.test_lessons_div_2__lessons_button.clicked.connect(self.test_lessons_div_2__lessons_button_toggled)
        self.ui.test_lessons_div_2__lessons_button.enterEvent = lambda x: enter_button(
            self.ui.test_lessons_div_2__lessons_button)
        self.ui.test_lessons_div_2__lessons_button.leaveEvent = self.leave_button

        self.ui.test_lessons_div_1__lessons_button.clicked.connect(self.test_lessons_div_1__lessons_button_toggled)
        self.ui.test_lessons_div_1__lessons_button.enterEvent = lambda x: enter_button(
            self.ui.test_lessons_div_1__lessons_button)
        self.ui.test_lessons_div_1__lessons_button.leaveEvent = self.leave_button

        self.ui.color_setting_div_1__colors_button.clicked.connect(self.color_setting_div_1__colors_button_toggled)
        self.ui.color_setting_div_1__colors_button.enterEvent = lambda x: enter_button(
            self.ui.color_setting_div_1__colors_button)
        self.ui.color_setting_div_1__colors_button.leaveEvent = self.leave_button

        self.ui.color_setting_div_2__color_button.clicked.connect(self.color_setting_div_2__color_button_toggled)
        self.ui.color_setting_div_2__color_button.enterEvent = lambda x: enter_button(
            self.ui.color_setting_div_2__color_button)
        self.ui.color_setting_div_2__color_button.leaveEvent = self.leave_button

        self.ui.color_setting_div_1__settings_button.clicked.connect(self.color_setting_div_1__settings_button_toggled)
        self.ui.color_setting_div_1__settings_button.enterEvent = lambda x: enter_button(
            self.ui.color_setting_div_1__settings_button)
        self.ui.color_setting_div_1__settings_button.leaveEvent = self.leave_button

        self.ui.color_setting_div_2__setting_button.clicked.connect(self.color_setting_div_2__setting_button_toggled)
        self.ui.color_setting_div_2__setting_button.enterEvent = lambda x: enter_button(
            self.ui.color_setting_div_2__setting_button)
        self.ui.color_setting_div_2__setting_button.leaveEvent = self.leave_button

        self.ui.about_profile_div_1__about_button.clicked.connect(self.about_profile_div_1__about_button_toggled)
        self.ui.about_profile_div_1__about_button.enterEvent = lambda x: enter_button(
            self.ui.about_profile_div_1__about_button)
        self.ui.about_profile_div_1__about_button.leaveEvent = self.leave_button

        self.ui.about_profile_div_2__about_button.clicked.connect(self.about_profile_div_2__about_button_toggled)
        self.ui.about_profile_div_2__about_button.enterEvent = lambda x: enter_button(
            self.ui.about_profile_div_2__about_button)
        self.ui.about_profile_div_2__about_button.leaveEvent = self.leave_button

        self.ui.about_profile_div_1__profile_button.clicked.connect(self.about_profile_div_1__profile_button_toggled)
        self.ui.about_profile_div_1__profile_button.enterEvent = lambda x: enter_button(
            self.ui.about_profile_div_1__profile_button)
        self.ui.about_profile_div_1__profile_button.leaveEvent = self.leave_button

        self.ui.about_profile_div_2__profile_button.clicked.connect(self.about_profile_div_2__profile_button_toggled)
        self.ui.about_profile_div_2__profile_button.enterEvent = lambda x: enter_button(
            self.ui.about_profile_div_2__profile_button)
        self.ui.about_profile_div_2__profile_button.leaveEvent = self.leave_button

        self.ui.burger.enterEvent = self.enter_for_burger
        self.ui.burger.leaveEvent = self.leave_for_burger
        self.ui.burger.clicked.connect(self.leave_button)

        self.ui.reset_language.enterEvent = self.enter_for_reset_language
        self.ui.reset_language.leaveEvent = self.leave_for_reset_language
        self.ui.reset_language.clicked.connect(self.leave_button)

    # function for change button's icon

    def enter_for_burger(self, event):
        self.ui.burger.setIcon(QtGui.QIcon('images/svg_icon/menu_orange.svg'))

    def leave_for_burger(self, event):
        self.ui.burger.setIcon(QtGui.QIcon('images/svg_icon/menu.svg'))

    def enter_for_reset_language(self, event):
        self.ui.reset_language.setIcon(QtGui.QIcon('images/svg_icon/globe_orange.svg'))

    def leave_for_reset_language(self, event):
        self.ui.reset_language.setIcon(QtGui.QIcon('images/svg_icon/globe.svg'))

    def leave_button(self, event):
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

        self.ui.stackedWidget.setCurrentIndex(2)
        self.focus = self.ui.color_setting_div_1__settings_button

    def color_setting_div_2__setting_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(2)
        self.focus = self.ui.color_setting_div_2__setting_button

    def about_profile_div_1__about_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(3)
        self.focus = self.ui.about_profile_div_1__about_button

    def about_profile_div_2__about_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(3)
        self.focus = self.ui.about_profile_div_2__about_button

    def about_profile_div_1__profile_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(4)
        self.focus = self.ui.about_profile_div_1__profile_button

    def about_profile_div_2__profile_button_toggled(self):

        self.ui.stackedWidget.setCurrentIndex(4)
        self.focus = self.ui.about_profile_div_2__profile_button

    def generate_text_for_test(self):
        global OLL_COUNT_LETTER, RIGHT_COUNT_LETTER
        global STRING
        generate_string()
        self.ui.given_text.setText(STRING)
        self.input_text.setText('')
        self.input_text.setFocus()
        LINEEDIT.write = True

    def generate_text_for_test_result(self):
        global OLL_COUNT_LETTER, RIGHT_COUNT_LETTER
        self.generate_text_for_test()
        self.ui.stackedWidget.setCurrentIndex(0)
        OLL_COUNT_LETTER = 0
        RIGHT_COUNT_LETTER = 0
        LINEEDIT.write = True

    def show_result(self, words, right, percent):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.value_wpm.setText(f'{words}')
        self.ui.lalue_cpm.setText(f'{right}')
        self.ui.value_percent_correct.setText(f'{int(percent * 100)}%')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    color = 'orange'
    style_file = colors.rewrite_qss('styles/main_style.qss', color)
    app.setStyleSheet(style_file)
    app.setStyleSheet(style_file)
    ex1 = WindowMain()
    ex1.show()

    sys.exit(app.exec())
