import sys
import random

import PyQt5.QtWidgets as qtw
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer

import colors
from blidingtype.main_ui import Ui_MainWindow
from work_with_db import login as lg
from checks import check_password, check_email, check_login
from work_with_db import registration, test_result, profile

flag = True


def enter_button(button):
    button.setFocus()


class LineEdit(qtw.QLineEdit):
    STRING = ''
    MODE = 'time'
    OLL_COUNT_LETTER = 0
    RIGHT_COUNT_LETTER = 0
    COUNT_WORDS = 0
    count_second = 0
    interval_time = 10
    write = True
    level = 'medium'

    code_key = [192, 49, 50, 51, 52, 53, 54, 55, 56, 57, 48, 189, 187, 220, 221, 219, 80, 79, 73, 85, 89, 84, 82,
                69,
                87, 81, 65, 83, 68, 70, 71, 72, 74, 75, 76, 186, 222, 191, 190, 188, 77, 78, 66, 86, 67, 88, 90, 32]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.isActive)

    def isActive(self):
        self.count_second += 1
        if self.count_second == self.interval_time:
            self.timer.stop()
            self.write = False
            self.count_second = 0
            print('таймер остановился')
            if ex1.ui.stackedWidget.currentIndex() == 0:
                WindowIndex.show_result(ex1, self.COUNT_WORDS, self.RIGHT_COUNT_LETTER,
                                        self.RIGHT_COUNT_LETTER / self.OLL_COUNT_LETTER)

    def keyPressEvent(self, e):
        self.setStyleSheet("""border: 1px solid rgba(0, 0, 0, 0);""")
        t, k = e.text(), e.nativeVirtualKey()

        if k in self.code_key and self.write:
            if self.OLL_COUNT_LETTER == 0:
                self.timer.start()
                print('таймер запустился')
            if self.STRING:
                self.OLL_COUNT_LETTER += 1
                if t == self.STRING[0]:
                    if len(self.STRING) > 1:
                        set_active_keyboard_button(self.STRING[1])
                    if t == ' ':
                        self.COUNT_WORDS += 1
                    super().keyPressEvent(e)
                    self.STRING = self.STRING[1:]
                    self.RIGHT_COUNT_LETTER += 1
                else:
                    wrong_letter()
            else:
                WindowIndex.generate_text_for_update(ex1)

    def generate_string(self):
        with open(f'data/{self.level}_words.txt', 'r', encoding='utf8') as f:
            f = f.read().split()
            s = ''
            while len(s) <= 55:
                s += random.choice(f) + ' '
            s = s[:s.rfind(' ')]
        self.write = True
        self.STRING = s
        set_active_keyboard_button(s[0])

        return s


def set_active_keyboard_button(char):
    if LIST_BUTTONS['active'] is None:
        style_active = """
            background-color: background-dominant2;
            color: background1000;"""
        style_active = colors.rewrite_qss_for_widget(style_active, color)
        LIST_BUTTONS[char].setStyleSheet(style_active)
        LIST_BUTTONS['active'] = LIST_BUTTONS[char]
    else:
        style_active = """
            background-color: background1000;
            color: background-dominant2;"""
        style_active = colors.rewrite_qss_for_widget(style_active, color)
        LIST_BUTTONS['active'].setStyleSheet(style_active)
        style_active = """
                    background-color: background-dominant2;
                    color: background1000;"""
        style_active = colors.rewrite_qss_for_widget(style_active, color)
        LIST_BUTTONS[char].setStyleSheet(style_active)
        LIST_BUTTONS['active'] = LIST_BUTTONS[char]


LINEEDIT: LineEdit
LIST_BUTTONS = {'active': None}


def wrong_letter():
    style_active = """border: 1px solid warning;"""
    style_active = colors.rewrite_qss_for_widget(style_active, color)
    LINEEDIT.setStyleSheet(style_active)


class WindowIndex(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.input_text = None
        self.focus = None
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
        global LINEEDIT
        self.ui.main_container.setCurrentIndex(3)
        self.ui.icon_menu_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.focus = self.ui.test_lessons_div_2__text_button
        self.ui.test_lessons_div_2__text_button.setFocus()

        self.input_text = LineEdit(self.ui.container_typed_text)
        self.input_text.setMinimumSize(QtCore.QSize(0, 90))
        self.input_text.setMaximumSize(QtCore.QSize(1300, 16777215))
        self.input_text.setText("")
        self.input_text.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.input_text.setObjectName("input_text")
        self.ui.verticalLayout_17.addWidget(self.input_text)
        self.input_text.setFocus()

        LINEEDIT = self.input_text
        self.create_list_buttons()
        self.ui.given_text.setText(LINEEDIT.generate_string())

        self.init_ui_main_window()

    def create_list_buttons(self):
        global LIST_BUTTONS
        for i in self.ui.line_1.children()[1:]:
            LIST_BUTTONS[i.text()] = i
        for i in self.ui.line_2.children()[1:]:
            LIST_BUTTONS[i.text()] = i
        for i in self.ui.line_3.children()[1:]:
            LIST_BUTTONS[i.text()] = i
        LIST_BUTTONS[' '] = self.ui.btn_spase

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

    def generate_text_for_test_result(self):
        s = LINEEDIT.generate_string()
        self.ui.given_text.setText(s)
        LINEEDIT.setText('')
        LINEEDIT.setFocus()
        self.ui.stackedWidget.setCurrentIndex(0)
        LINEEDIT.OLL_COUNT_LETTER = 0
        LINEEDIT.RIGHT_COUNT_LETTER = 0
        LINEEDIT.COUNT_WORDS = 0
        LINEEDIT.count_second = 0

    def generate_text_for_update(self):
        s = LINEEDIT.generate_string()
        self.ui.given_text.setText(s)
        LINEEDIT.setText('')
        LINEEDIT.setFocus()
        self.ui.stackedWidget.setCurrentIndex(0)

    def init_ui_main_window(self):
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
        LINEEDIT.setFocus()
        self.ui.given_text.setText(LINEEDIT.generate_string())
        self.input_text.setText('')
        self.input_text.setFocus()

    def test_lessons_div_2__text_button_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.focus = self.ui.test_lessons_div_2__text_button
        LINEEDIT.setFocus()
        self.ui.given_text.setText(LINEEDIT.generate_string())
        self.input_text.setText('')
        self.input_text.setFocus()

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
        self.go_to_profile()

    def about_profile_div_2__profile_button_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.focus = self.ui.about_profile_div_2__profile_button
        self.go_to_profile()

    def go_to_profile(self):
        wpm, cpm, accuracy = profile.get_oll_result(profile.get_id_user())
        self.ui.profile_value_wpm.setText(str(max(wpm)))
        self.ui.profile_value_percent.setText(str(max(accuracy)))
        self.ui.profile_value_cpm.setText(str(max(cpm)))
        self.ui.profile_avg_value_wpm.setText(str(int(sum(wpm) / len(wpm))))
        self.ui.profile_avg_value_percent.setText(str(int(sum(accuracy) / len(accuracy))))
        self.ui.profile_avg_value_cpm.setText(str(int(sum(cpm) / len(cpm))))

    def show_result(self, wpm, cpm, accuracy):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.value_wpm.setText(f'{wpm}')
        self.ui.value_cpm.setText(f'{cpm}')
        self.ui.value_percent_correct.setText(f'{int(accuracy * 100)}%')

        # запись результатов в бд
        test_result.write_test_result_in_db(wpm, cpm, int(accuracy * 100))


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    color = 'orange'

    style_file = colors.rewrite_qss('styles/style.qss', color)
    app.setStyleSheet(style_file)

    ex1 = WindowIndex()
    ex1.showMaximized()

    sys.exit(app.exec())
