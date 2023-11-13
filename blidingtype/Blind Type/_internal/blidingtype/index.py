import sys
import random

import PyQt5.QtWidgets as qtw
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer, QEvent

import colors
from blidingtype.index_ui import Ui_MainWindow
from work_with_db import login as lg
from checks import check_password, check_email, check_login
from work_with_db import registration, test_result, profile

color: str
app = None
SYS_PATH = 'C:/Users/Professional/PycharmProjects/pythonProject/blidingtype'  # абсолютный путь до файлов


def change_color(button):
    with open(f'{SYS_PATH}/data/color.txt', 'w',
              encoding='utf8') as f:
        f.write(str(button.objectName().replace('change_color_', '')))
        f.close()

        WindowIndex.restart()


def read_color():
    global color
    with open(f'{SYS_PATH}/data/color.txt') as color:
        color = color.read()


def change_setting():
    with open(f'{SYS_PATH}/data/settings.txt') as settings:
        settings = [i.rstrip() for i in settings.readlines()]
        return settings


def check_login_people():
    global flag
    try:
        with open(f'{SYS_PATH}/data/login_data.txt', 'r',
                  encoding='utf8') as data_person:
            data = data_person.readlines()
            if len(data) == 2:
                login, password = [i.rstrip() for i in data]
                flag = True
                if login.count('@') == 0:
                    lg.check_cor_password_in_db_login(login, password)
                else:
                    lg.check_cor_password_in_db_email(login, password)
            elif len(data) == 0 or len(data) == 1:
                flag = False
                print('пользователь не зарегистрировался')
    except lg.IncorrectPassword:
        flag = False
        print('пароль не совпадает')
    except FileNotFoundError as er:
        flag = False
        print(er, 'файл не найден')


class LineEdit(qtw.QLineEdit):
    STRING = ''
    MODE = 'time'
    OLL_COUNT_LETTER = 0
    RIGHT_COUNT_LETTER = 0
    COUNT_WORDS = 0
    count_second = 0
    interval_time = 60
    write = True
    level = 'easy'

    code_key = [192, 49, 50, 51, 52, 53, 54, 55, 56, 57, 48, 189, 187, 220, 221, 219, 80, 79, 73, 85, 89, 84, 82,
                69, 87, 81, 65, 83, 68, 70, 71, 72, 74, 75, 76, 186, 222, 191, 190, 188, 77, 78, 66, 86, 67, 88, 90, 32]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tic_tac)

    def tic_tac(self):  # таймер
        self.count_second += 1
        if self.count_second == self.interval_time:
            self.timer.stop()
            self.write = False
            self.count_second = 0
            if WindowIndex.singleton.ui.stackedWidget.currentIndex() == 0:
                WindowIndex.show_result(WindowIndex.singleton, self.COUNT_WORDS, self.RIGHT_COUNT_LETTER,
                                        self.RIGHT_COUNT_LETTER / self.OLL_COUNT_LETTER)

    def keyPressEvent(self, e):
        style_active = """
            background-color: rgba(0, 0, 0, 0);
            font-size: 40px;
            outline: none;    
            color: background-dominant2;
            border: 0px;
            border-bottom: 1px solid background-dominant1;"""
        style_active = colors.rewrite_qss_for_widget(style_active, color)
        self.setStyleSheet(style_active)  # применяем стиль к LINEEDIT

        t, k = e.text(), e.nativeVirtualKey()  # берём текст клавиши и её код

        if k in self.code_key and self.write:  # проверка нажатой клавиши
            if self.OLL_COUNT_LETTER == 0:
                self.timer.start()
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
                WindowIndex.generate_text_for_update(WindowIndex.singleton)

    def generate_string(self):  # генерация строки для given_text
        with open(f'{SYS_PATH}/data/{self.level}_words.txt', 'r',
                  encoding='utf8') as f:
            f = f.read().split()
            s = ''
            while len(s) <= 55:
                s += random.choice(f) + ' '
            s = s[:s.rfind(' ')]
        self.write = True
        self.STRING = s
        set_active_keyboard_button(s[0])

        return s


def set_active_keyboard_button(char):  # меняем цвет клавиши, которую нужно нажать для правильного ответа
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
    style_active = """border: 0px;
    border-bottom: 1px solid warning;
    background-color: rgba(0, 0, 0, 0);
    font-size: 40px;
    outline: none;    
    color: background-dominant2;"""
    style_active = colors.rewrite_qss_for_widget(style_active, color)
    LINEEDIT.setStyleSheet(style_active)


# анимации кнопок в menu в main
def enter_button_2(button):
    button.setIcon(QtGui.QIcon(
        f'{SYS_PATH}/images/{color}/{button.objectName()[:-2]}_active.svg'))


def leave_button_2(button):
    button.setIcon(QtGui.QIcon(
        f'{SYS_PATH}/images/{color}/{button.objectName()[:-2]}_inactive.svg'))


class WindowIndex(qtw.QMainWindow):  # класс приложения
    singleton: 'WindowIndex' = None
    global app

    def __init__(self):
        super().__init__()
        self.buttons = []
        self.input_text = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.showMaximized()

        check_login_people()  # проверка на то, что пользователь ранее входил в аккаунт
        if not flag:
            self.go_to_preview()
        else:
            self.go_to_login()

        self.focus = self.ui.test_2  # переменные для main.menu
        self.last_focus = self.ui.test_2
        self.select_focus(self.ui.test_2)

    @staticmethod
    def restart():  # метод перезагрузки окна, когда происходит изменение цвета
        msg = qtw.QMessageBox()  # создаём окна для подтверждения перезагрузки
        msg.setWindowTitle("Изменение цветовой палитры")
        msg.setText('Для изменения цвета нужно перезагрузить приложение')
        msg.setIcon(qtw.QMessageBox.Warning)
        msg.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        msg.setDefaultButton(qtw.QMessageBox.Ok)

        res = msg.exec()

        if res == qtw.QMessageBox.Ok:  # если пользователь нажал Ok, то перезапускаем приложение
            WindowIndex.singleton.close()
            read_color()
            style_file = colors.rewrite_qss(f'{SYS_PATH}/styles/style.qss', color)
            app.setStyleSheet(style_file)
            WindowIndex.singleton = WindowIndex()
            WindowIndex.singleton.setWindowIcon(QtGui.QIcon(f'{SYS_PATH}/images/{color}/logo.svg'))
            WindowIndex.singleton.setWindowTitle('Blind Typing')
        else:
            for i in WindowIndex.singleton.ui.color_page_container.children()[1:]:
                if i.objectName().replace('change_color_', '') == color:
                    i.setFocus()

    @staticmethod
    def start():  # функция для первого создания приложения
        read_color()
        style_file = colors.rewrite_qss(
            f'{SYS_PATH}/styles/style.qss',
            color)
        app.setStyleSheet(style_file)
        WindowIndex.singleton = WindowIndex()
        WindowIndex.singleton.setWindowIcon(QtGui.QIcon(f'{SYS_PATH}/images/{color}/logo.svg'))
        WindowIndex.singleton.setWindowTitle('Blind Typing')

    def initUI(self):  # присваиваем иконкам значения
        self.ui.login_error.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/error_inactive.svg'))
        self.ui.change_password_error.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/error_inactive.svg'))
        self.ui.registration_error.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/error_inactive.svg'))
        self.ui.logo_icon_1.setIcon(
            QtGui.QIcon(f'{SYS_PATH}/images/{color}/logo.svg'))
        self.ui.logo_icon_2.setIcon(
            QtGui.QIcon(f'{SYS_PATH}/images/{color}/logo.svg'))
        self.ui.preview_logo.setIcon(
            QtGui.QIcon(f'{SYS_PATH}/images/{color}/logo_big.svg'))
        self.ui.login_show_password.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/eye_inactive.svg'))

        self.ui.refrech_button.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/refresh_inactive.svg'))
        self.ui.refrech_button_2.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/refresh_inactive.svg'))
        self.ui.next_test_button.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/next_test_inactive.svg'))
        self.ui.registration_show_password.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/eye_inactive.svg'))
        self.ui.change_password_show_password.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/eye_inactive.svg'))

        self.ui.test_1.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.test_1.objectName()[:-2]}_inactive.svg'))
        self.ui.lessons_1.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.lessons_1.objectName()[:-2]}_inactive.svg'))
        self.ui.colors_1.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.colors_1.objectName()[:-2]}_inactive.svg'))
        self.ui.settings_1.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.settings_1.objectName()[:-2]}_inactive.svg'))
        self.ui.about_1.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.about_1.objectName()[:-2]}_inactive.svg'))
        self.ui.profile_1.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.profile_1.objectName()[:-2]}_inactive.svg'))

        self.ui.test_2.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.test_2.objectName()[:-2]}_inactive.svg'))
        self.ui.lessons_2.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.lessons_2.objectName()[:-2]}_inactive.svg'))
        self.ui.colors_2.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.colors_2.objectName()[:-2]}_inactive.svg'))
        self.ui.settings_2.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.settings_2.objectName()[:-2]}_inactive.svg'))
        self.ui.about_2.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.about_2.objectName()[:-2]}_inactive.svg'))
        self.ui.profile_2.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.profile_2.objectName()[:-2]}_inactive.svg'))

        self.ui.burger_1.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.ui.burger_1.objectName()[:-2]}_inactive.svg'))

    # функции переходов между разделами ================================
    def go_to_preview(self):
        self.ui.main_container.setCurrentIndex(0)
        self.ui.preview_registration_button.clicked.connect(self.go_to_registration)
        self.ui.preview_login_button.clicked.connect(self.go_to_login)

    def go_to_login(self):
        self.ui.login_password_edit.setEchoMode(qtw.QLineEdit.EchoMode.Password)
        self.ui.main_container.setCurrentIndex(1)
        self.ui.login_login_button.clicked.connect(self.login_data_validity_check)
        self.login_hide_error()
        self.ui.login_registration_button.clicked.connect(self.go_to_registration)
        self.ui.login_show_password.clicked.connect(lambda x: self.change_echo_mode(self.ui.login_show_password))
        self.ui.login_password_edit.installEventFilter(self)
        self.ui.change_password_button.clicked.connect(self.go_to_change_password)
        self.ui.login_show_password.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/eye_inactive.svg'))

        self.ui.registration_show_password.clicked.connect(
            lambda x: self.change_echo_mode(self.ui.registration_show_password))
        self.ui.change_password_show_password.clicked.connect(
            lambda x: self.change_echo_mode(self.ui.change_password_show_password))

        with open(f'{SYS_PATH}/data/login_data.txt', 'r',
                  encoding='utf8') as data_person:
            data = data_person.readlines()  # берём из файла сохранённый логин и пароль
        if data:
            self.ui.login_login_edit.setText(data[0].rstrip())  # записываем их в edits
            self.ui.login_password_edit.setText(data[1].rstrip())

    def go_to_change_password(self):
        self.ui.change_password_edit.setEchoMode(qtw.QLineEdit.EchoMode.Password)
        self.ui.main_container.setCurrentIndex(4)
        self.ui.change_password_edit.installEventFilter(self)
        self.ui.change_password_login_button.clicked.connect(self.change_password_data_validity_check)
        self.ui.change_password_login_button_2.clicked.connect(self.go_to_login)
        self.change_password_hide_error()

    def go_to_registration(self):
        self.ui.registration_password_edit.setEchoMode(qtw.QLineEdit.EchoMode.Password)
        self.ui.main_container.setCurrentIndex(2)
        self.ui.registration_register_button.clicked.connect(self.registration_data_validity_check)
        self.registration_hide_error()
        self.ui.registration_login_button.clicked.connect(self.go_to_login)
        self.ui.registration_password_edit.installEventFilter(self)

    def go_to_main(self):
        global LINEEDIT
        self.ui.main_container.setCurrentIndex(3)
        self.ui.icon_menu_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.title_window.setText('Клавиатурный Тренажер')

        self.ui.easy_level_button.clicked.connect(self.change_level_of_generate_text)
        self.ui.medium_level_button.clicked.connect(self.change_level_of_generate_text)
        self.ui.hard_level_button.clicked.connect(self.change_level_of_generate_text)

        if len(self.ui.container_typed_text.children()) < 3:
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

    def go_to_profile(self):
        wpm, cpm, accuracy = profile.get_oll_result(profile.get_id_user())
        self.ui.profile_value_wpm.setText(str(max(wpm)))
        self.ui.profile_value_percent.setText(str(max(accuracy)) + '%')
        self.ui.profile_value_cpm.setText(str(max(cpm)))
        self.ui.profile_avg_value_wpm.setText(str(int(sum(wpm) / len(wpm))))
        self.ui.profile_avg_value_percent.setText(str(int(sum(accuracy) / len(accuracy))) + '%')
        self.ui.profile_avg_value_cpm.setText(str(int(sum(cpm) / len(cpm))))

    # анимации ====================================================
    def eventFilter(self, obj, event):
        style_active = """background: none;
                    outline: none;
                    border-top-right-radius: 5px;
                    border-bottom-right-radius: 5px;
                    border: 1px solid active;
                    border-left: 0px;
                    padding: 11px 15px 10px 6px;
                    """
        style_inactive = """background: none;
                    outline: none;
                    border-top-right-radius: 5px;
                    border-bottom-right-radius: 5px;
                    border: 1px solid inactive;
                    border-left: 0px;
                    padding: 11px 15px 10px 6px;
                    """
        style_active = colors.rewrite_qss_for_widget(style_active, color)
        style_inactive = colors.rewrite_qss_for_widget(style_inactive, color)
        if obj == self.ui.login_password_edit and event.type() == QEvent.FocusIn:
            self.ui.login_show_password.setStyleSheet(style_active)
        if obj == self.ui.registration_password_edit and event.type() == QEvent.FocusIn:
            self.ui.registration_show_password.setStyleSheet(style_active)

        if obj == self.ui.login_password_edit and event.type() == QEvent.FocusOut:
            self.ui.login_show_password.setStyleSheet(style_inactive)
        if obj == self.ui.registration_password_edit and event.type() == QEvent.FocusOut:
            self.ui.registration_show_password.setStyleSheet(style_inactive)

        if obj == self.ui.change_password_edit and event.type() == QEvent.FocusIn:
            self.ui.change_password_show_password.setStyleSheet(style_active)
        if obj == self.ui.change_password_edit and event.type() == QEvent.FocusOut:
            self.ui.change_password_show_password.setStyleSheet(style_inactive)

        return False

    def leave_button(self, button):
        button.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{button.objectName()[:-2]}_inactive.svg'))
        self.last_focus.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.last_focus.objectName()[:-2]}_inactive.svg'))
        self.focus.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.focus.objectName()[:-2]}_active.svg'))

        style_active = """color: active;"""
        style_inactive = """color: inactive;"""
        style_active = colors.rewrite_qss_for_widget(style_active, color)
        style_inactive = colors.rewrite_qss_for_widget(style_inactive, color)
        button.setStyleSheet(style_inactive)
        self.last_focus.setStyleSheet(style_inactive)
        self.focus.setStyleSheet(style_active)

    def enter_button(self, button):
        self.focus.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{self.focus.objectName()[:-2]}_inactive.svg'))
        button.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{button.objectName()[:-2]}_active.svg'))

        style_active = """color: active;"""
        style_inactive = """color: inactive;"""
        style_active = colors.rewrite_qss_for_widget(style_active, color)
        style_inactive = colors.rewrite_qss_for_widget(style_inactive, color)
        self.focus.setStyleSheet(style_inactive)
        button.setStyleSheet(style_active)

    def select_focus(self, button):
        button.setIcon(QtGui.QIcon(
            f'{SYS_PATH}/images/{color}/{button.objectName()[:-2]}_active.svg'))
        style_active = colors.rewrite_qss_for_widget("""color: active;""", color)
        self.focus = button
        button.setStyleSheet(style_active)

    def change_echo_mode(self, button):
        if button == self.ui.login_show_password:
            if self.ui.login_password_edit.echoMode() == qtw.QLineEdit.EchoMode.Password:
                self.ui.login_password_edit.setEchoMode(qtw.QLineEdit.EchoMode.Normal)
                self.ui.login_show_password.setIcon(QtGui.QIcon(
                    f'{SYS_PATH}/images/{color}/eye_active.svg'))
            else:
                self.ui.login_password_edit.setEchoMode(qtw.QLineEdit.EchoMode.Password)
                self.ui.login_show_password.setIcon(QtGui.QIcon(
                    f'{SYS_PATH}/images/{color}/eye_inactive.svg'))
            self.ui.login_password_edit.setFocus()
        elif button == self.ui.registration_show_password:
            if self.ui.registration_password_edit.echoMode() == qtw.QLineEdit.EchoMode.Password:
                self.ui.registration_password_edit.setEchoMode(qtw.QLineEdit.EchoMode.Normal)
                self.ui.registration_show_password.setIcon(QtGui.QIcon(
                    f'{SYS_PATH}/images/{color}/eye_active.svg'))
            else:
                self.ui.registration_password_edit.setEchoMode(qtw.QLineEdit.EchoMode.Password)
                self.ui.registration_show_password.setIcon(QtGui.QIcon(
                    f'{SYS_PATH}/images/{color}/eye_inactive.svg'))
            self.ui.registration_password_edit.setFocus()
        elif button == self.ui.change_password_show_password:
            if self.ui.change_password_edit.echoMode() == qtw.QLineEdit.EchoMode.Password:
                self.ui.change_password_edit.setEchoMode(qtw.QLineEdit.EchoMode.Normal)
                self.ui.change_password_show_password.setIcon(QtGui.QIcon(
                    f'{SYS_PATH}/images/{color}/eye_active.svg'))
            else:
                self.ui.change_password_edit.setEchoMode(qtw.QLineEdit.EchoMode.Password)
                self.ui.change_password_show_password.setIcon(QtGui.QIcon(
                    f'{SYS_PATH}/images/{color}/eye_inactive.svg'))
            self.ui.change_password_edit.setFocus()

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
            if login.count('@') == 0:
                lg.check_login_in_db(login)
                lg.check_cor_password_in_db_login(login, password)
            else:
                lg.check_email_in_db(login)
                lg.check_cor_password_in_db_email(login, password)

        except lg.NotLoginInDb:
            text_error = 'Пользователь не зарегиcтрирован'
            self.login_show_error()
        except lg.IncorrectPassword:
            text_error = 'Неверный пароль'
            self.login_show_error()
        except lg.NotEmailInDb:
            text_error = 'Пользователь с такой почтой не зарегистрировался'
            self.login_show_error()

        if text_error == '':
            self.login_hide_error()
            self.go_to_main()
            with open(f'{SYS_PATH}/data/login_data.txt', 'w',
                      encoding='utf8') as data_person:
                data_person.write(login + '\n')
                data_person.write(password)

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

    def registration_data_validity_check(self):  # проверка написания пароля
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

    # change_password ================================================================================
    def change_password_hide_error(self):
        self.ui.change_password_error_label.hide()
        self.ui.change_password_error.hide()
        self.ui.change_password_error_container.hide()

    def change_password_show_error(self):
        self.ui.change_password_error_label.show()
        self.ui.change_password_error.show()
        self.ui.change_password_error_container.show()

    def change_password_data_validity_check(self):  # проверяем данные в change_password
        login = self.ui.change_password_login_edit.text()
        password = self.ui.change_password_edit.text()
        text_error = ''

        try:  # check password
            check_password.check_password(password)
        except check_password.LengthError:
            text_error = 'Пароль должен быть длинной не менее 8 символов'
            self.change_password_show_error()
        except check_password.LetterError:
            text_error = 'Пароль должен иметь буквы разного регистра'
            self.change_password_show_error()
        except check_password.DigitError:
            text_error = 'Пароль должен иметь цифры'
            self.change_password_show_error()
        except check_password.SequenceError:
            text_error = 'Пароль не должен содержать комбинации символов'
            self.change_password_show_error()

        except check_password.SpaceError:
            text_error = 'Пароль не должен содержать пробелов'
            self.change_password_show_error()

        try:
            if login.count('@') == 0:
                lg.check_login_in_db(login)
            else:
                lg.check_email_in_db(login)

        except lg.NotLoginInDb:
            text_error = 'Пользователь не зарегиcтрирован'
            self.change_password_show_error()
        except lg.NotEmailInDb:
            text_error = 'Пользователь с такой почтой не зарегистрировался'
            self.change_password_show_error()

        self.ui.change_password_error_label.setText(text_error)
        if self.ui.registration_error_label.text() == '':
            self.change_password_hide_error()
            lg.change_password(login, password)
            self.go_to_login()

    # main ================================================================================

    def create_list_buttons(self):  # создаём лист кноп для отображения подсказки (какую кнопку надо нажать)
        global LIST_BUTTONS
        for i in self.ui.line_1.children()[1:]:
            LIST_BUTTONS[i.text()] = i
        for i in self.ui.line_2.children()[1:]:
            LIST_BUTTONS[i.text()] = i
        for i in self.ui.line_3.children()[1:]:
            LIST_BUTTONS[i.text()] = i
        LIST_BUTTONS[' '] = self.ui.btn_spase

    def change_level_of_generate_text(self):  # изменяем уровень сложности теста
        but = self.sender()
        if but == self.ui.easy_level_button:
            LINEEDIT.level = 'easy'
        elif but == self.ui.medium_level_button:
            LINEEDIT.level = 'medium'
        elif but == self.ui.hard_level_button:
            LINEEDIT.level = 'hard'
        self.generate_text_for_test_result()

    def generate_text_for_test_result(self):  # генерация строки если начали тест заново
        s = LINEEDIT.generate_string()
        self.ui.given_text.setText(s)
        LINEEDIT.setText('')
        LINEEDIT.setFocus()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.title_window.setText('Клавиатурный Тренажер')
        LINEEDIT.OLL_COUNT_LETTER = 0
        LINEEDIT.RIGHT_COUNT_LETTER = 0
        LINEEDIT.COUNT_WORDS = 0
        LINEEDIT.count_second = 0

    def generate_text_for_update(self):  # генерация строки для продолжения текста
        s = LINEEDIT.generate_string()
        self.ui.given_text.setText(s)
        LINEEDIT.setText('')
        LINEEDIT.setFocus()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.title_window.setText('Клавиатурный Тренажер')

    def init_ui_main_window(self):  # задаём сигналы для кнопок в main
        self.ui.refrech_button.clicked.connect(self.generate_text_for_test_result)
        self.ui.next_test_button.clicked.connect(self.generate_text_for_test_result)
        self.ui.refrech_button_2.setEnabled(False)

        self.ui.test_1.clicked.connect(self.test_1)
        self.ui.test_1.enterEvent = lambda x: self.enter_button(self.ui.test_1)
        self.ui.test_1.leaveEvent = lambda x: self.leave_button(self.ui.test_1)

        self.ui.test_2.clicked.connect(self.test_2)
        self.ui.test_2.enterEvent = lambda x: self.enter_button(self.ui.test_2)
        self.ui.test_2.leaveEvent = lambda x: self.leave_button(self.ui.test_2)

        self.ui.lessons_2.clicked.connect(self.lessons_2)
        self.ui.lessons_2.enterEvent = lambda x: self.enter_button(self.ui.lessons_2)
        self.ui.lessons_2.leaveEvent = lambda x: self.leave_button(self.ui.lessons_2)

        self.ui.lessons_1.clicked.connect(self.lessons_1)
        self.ui.lessons_1.enterEvent = lambda x: self.enter_button(self.ui.lessons_1)
        self.ui.lessons_1.leaveEvent = lambda x: self.leave_button(self.ui.lessons_1)

        self.ui.colors_1.clicked.connect(self.colors_1)
        self.ui.colors_1.enterEvent = lambda x: self.enter_button(self.ui.colors_1)
        self.ui.colors_1.leaveEvent = lambda x: self.leave_button(self.ui.colors_1)

        self.ui.colors_2.clicked.connect(self.colors_2)
        self.ui.colors_2.enterEvent = lambda x: self.enter_button(self.ui.colors_2)
        self.ui.colors_2.leaveEvent = lambda x: self.leave_button(self.ui.colors_2)

        self.ui.settings_1.clicked.connect(self.settings_1)
        self.ui.settings_1.enterEvent = lambda x: self.enter_button(self.ui.settings_1)
        self.ui.settings_1.leaveEvent = lambda x: self.leave_button(self.ui.settings_1)

        self.ui.settings_2.clicked.connect(self.settings_2)
        self.ui.settings_2.enterEvent = lambda x: self.enter_button(self.ui.settings_2)
        self.ui.settings_2.leaveEvent = lambda x: self.leave_button(self.ui.settings_2)

        self.ui.about_1.clicked.connect(self.about_1)
        self.ui.about_1.enterEvent = lambda x: self.enter_button(self.ui.about_1)
        self.ui.about_1.leaveEvent = lambda x: self.leave_button(self.ui.about_1)

        self.ui.about_2.clicked.connect(self.about_2)
        self.ui.about_2.enterEvent = lambda x: self.enter_button(self.ui.about_2)
        self.ui.about_2.leaveEvent = lambda x: self.leave_button(self.ui.about_2)

        self.ui.profile_1.clicked.connect(self.profile_1)
        self.ui.profile_1.enterEvent = lambda x: self.enter_button(self.ui.profile_1)
        self.ui.profile_1.leaveEvent = lambda x: self.leave_button(self.ui.profile_1)

        self.ui.profile_2.clicked.connect(self.profile_2)
        self.ui.profile_2.enterEvent = lambda x: self.enter_button(self.ui.profile_2)
        self.ui.profile_2.leaveEvent = lambda x: self.leave_button(self.ui.profile_2)

        self.ui.burger_1.clicked.connect(self.burger_1)
        self.ui.burger_1.enterEvent = lambda x: enter_button_2(self.ui.burger_1)
        self.ui.burger_1.leaveEvent = lambda x: leave_button_2(self.ui.burger_1)

        self.ui.reset_language_1.clicked.connect(self.reset_language_1)
        self.ui.reset_language_1.enterEvent = lambda x: enter_button_2(self.ui.reset_language_1)
        self.ui.reset_language_1.leaveEvent = lambda x: leave_button_2(self.ui.reset_language_1)

        self.ui.change_color_black_and_white.clicked.connect(
            lambda x: change_color(self.ui.change_color_black_and_white))
        self.ui.change_color_native_dark.clicked.connect(
            lambda x: change_color(self.ui.change_color_native_dark))
        self.ui.change_color_orange.clicked.connect(
            lambda x: change_color(self.ui.change_color_orange))
        self.ui.change_color_redux_dark.clicked.connect(
            lambda x: change_color(self.ui.change_color_redux_dark))
        self.ui.change_color_vs_code.clicked.connect(
            lambda x: change_color(self.ui.change_color_vs_code))

        #  function for changing menu page

    def set_focus(self, index):  # для burger
        lst_hidden = [self.ui.test_2, self.ui.lessons_2, self.ui.colors_2, self.ui.settings_2, self.ui.about_2,
                      self.ui.profile_2]
        lst_show = [self.ui.test_1, self.ui.lessons_1, self.ui.colors_1, self.ui.settings_1, self.ui.about_1,
                    self.ui.profile_1]
        if self.ui.icon_menu_widget.isHidden():
            self.focus = lst_hidden[index]
            self.last_focus = lst_hidden[index]
            self.leave_button(self.focus)
        else:
            self.focus = lst_show[index]
            self.last_focus = lst_show[index]
            self.leave_button(self.focus)

    def burger_1(self):  # анимации при нажатии burger (сделать кнопку для текущего раздела active)

        index = self.ui.stackedWidget.currentIndex()

        if index == 0:
            self.set_focus(0)
        elif index == 1:
            self.set_focus(1)
        elif index == 2:
            self.set_focus(3)
        elif index == 3:
            self.set_focus(4)
        elif index == 4:
            self.set_focus(5)
        elif index == 5:
            self.set_focus(1)
        elif index == 6:
            self.set_focus(2)

    def reset_language_1(
            self):  # это нет потому что мне лень каждую строку вносить в пременную и по отдельности задавать
        pass

    #  переходы к разным разделам =========================================================
    def test_1(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.title_window.setText('Клавиатурный Тренажер')
        self.last_focus = self.focus
        self.focus = self.ui.test_1

        LINEEDIT.setFocus()
        self.ui.given_text.setText(LINEEDIT.generate_string())
        self.input_text.setText('')
        self.input_text.setFocus()

    def test_2(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.title_window.setText('Клавиатурный Тренажер')
        self.last_focus = self.focus
        self.focus = self.ui.test_2
        LINEEDIT.setFocus()
        self.ui.given_text.setText(LINEEDIT.generate_string())
        self.input_text.setText('')
        self.input_text.setFocus()

    def lessons_2(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.title_window.setText('Уроки слепой печати')
        self.last_focus = self.focus
        self.focus = self.ui.lessons_2

    def lessons_1(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.title_window.setText('Уроки слепой печати')
        self.last_focus = self.focus
        self.focus = self.ui.lessons_1

    def colors_1(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.title_window.setText('Цвета')
        self.last_focus = self.focus
        self.focus = self.ui.colors_1
        for i in self.ui.color_page_container.children()[1:]:
            if i.objectName().replace('change_color_', '') == color:
                i.setFocus()

    def colors_2(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.title_window.setText('Цвета')
        self.last_focus = self.focus
        self.focus = self.ui.colors_2
        for i in self.ui.color_page_container.children()[1:]:
            if i.objectName().replace('change_color_', '') == color:
                i.setFocus()

    def settings_1(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.title_window.setText('Настройки')
        self.last_focus = self.focus
        self.focus = self.ui.settings_1
        settings = change_setting()

        self.ui.keyboard_setting_radio_button.toggled.connect(self.change_setting_2)
        if settings[0] == 'True':
            self.ui.keyboard.show()
            self.ui.keyboard_setting_radio_button.setChecked(True)
        else:
            self.ui.keyboard.hide()
            self.ui.keyboard_setting_radio_button.setChecked(False)

    def settings_2(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.title_window.setText('Настройки')
        self.last_focus = self.focus
        self.focus = self.ui.settings_2
        settings = change_setting()
        self.ui.keyboard_setting_radio_button.toggled.connect(self.change_setting_2)
        if settings[0] == 'True':
            self.ui.keyboard.show()
            self.ui.keyboard_setting_radio_button.setChecked(True)
        else:
            self.ui.keyboard.hide()
            self.ui.keyboard_setting_radio_button.setChecked(False)

    def change_setting_2(self):  # запись в файл последнего состояния клавиатуры (show, hide) (True, False)
        with open(f'{SYS_PATH}/data/settings.txt', 'w',
                  encoding='utf8') as settings:
            if self.ui.keyboard_setting_radio_button.isChecked():
                settings.write('True')
            else:
                settings.write('False')
        settings = change_setting()
        if settings[0] == 'True':
            self.ui.keyboard.show()
        else:
            self.ui.keyboard.hide()

    def about_1(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.title_window.setText('О приложении')
        self.last_focus = self.focus
        self.focus = self.ui.about_1

    def about_2(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.title_window.setText('О приложении')
        self.last_focus = self.focus
        self.focus = self.ui.about_2

    def profile_1(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.title_window.setText('Профиль')
        self.last_focus = self.focus
        self.focus = self.ui.profile_1

        self.go_to_profile()

    def profile_2(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.title_window.setText('Профиль')
        self.last_focus = self.focus
        self.focus = self.ui.profile_2
        self.go_to_profile()

    def show_result(self, wpm, cpm, accuracy):  # показываем результаты после теста
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.title_window.setText('Результаты текста')

        self.ui.value_wpm.setText(f'{wpm}')
        self.ui.value_cpm.setText(f'{cpm}')
        self.ui.value_percent_correct.setText(f'{int(accuracy * 100)}%')

        # запись результатов в бд
        test_result.write_test_result_in_db(wpm, cpm, int(accuracy * 100))


def main():
    global app
    app = qtw.QApplication(sys.argv)
    WindowIndex.start()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
