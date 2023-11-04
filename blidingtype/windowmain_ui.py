# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blidingtype/designs/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1900, 1199)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 10, 0, 20)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.header_widget = QtWidgets.QFrame(self.centralwidget)
        self.header_widget.setMinimumSize(QtCore.QSize(0, 90))
        self.header_widget.setMaximumSize(QtCore.QSize(16777215, 90))
        self.header_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_widget.setObjectName("header_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.burger = QtWidgets.QPushButton(self.header_widget)
        self.burger.setMinimumSize(QtCore.QSize(50, 50))
        self.burger.setMaximumSize(QtCore.QSize(50, 50))
        self.burger.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/svg_icon/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.burger.setIcon(icon)
        self.burger.setIconSize(QtCore.QSize(48, 58))
        self.burger.setCheckable(True)
        self.burger.setAutoExclusive(False)
        self.burger.setObjectName("burger")
        self.horizontalLayout_2.addWidget(self.burger)
        self.title_window = QtWidgets.QLabel(self.header_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.title_window.setFont(font)
        self.title_window.setObjectName("title_window")
        self.horizontalLayout_2.addWidget(self.title_window)
        spacerItem = QtWidgets.QSpacerItem(393, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.reset_language = QtWidgets.QPushButton(self.header_widget)
        self.reset_language.setMinimumSize(QtCore.QSize(50, 50))
        self.reset_language.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/svg_icon/globe.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_language.setIcon(icon1)
        self.reset_language.setIconSize(QtCore.QSize(48, 48))
        self.reset_language.setCheckable(False)
        self.reset_language.setAutoExclusive(False)
        self.reset_language.setObjectName("reset_language")
        self.horizontalLayout_2.addWidget(self.reset_language)
        self.gridLayout.addWidget(self.header_widget, 0, 2, 1, 1)
        self.main_widget = QtWidgets.QFrame(self.centralwidget)
        self.main_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_widget.setObjectName("main_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.test = QtWidgets.QWidget()
        self.test.setObjectName("test")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.test)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.test)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.stackedWidget.addWidget(self.test)
        self.lessons = QtWidgets.QWidget()
        self.lessons.setObjectName("lessons")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.lessons)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.lessons)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.lessons)
        self.colors = QtWidgets.QWidget()
        self.colors.setObjectName("colors")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.colors)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.colors)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.colors)
        self.setting = QtWidgets.QWidget()
        self.setting.setObjectName("setting")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.setting)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.setting)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.stackedWidget.addWidget(self.setting)
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.about)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.about)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.stackedWidget.addWidget(self.about)
        self.profile = QtWidgets.QWidget()
        self.profile.setObjectName("profile")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.profile)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.profile)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.stackedWidget.addWidget(self.profile)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.main_widget, 1, 2, 1, 1)
        self.full_menu_widget = QtWidgets.QFrame(self.centralwidget)
        self.full_menu_widget.setMinimumSize(QtCore.QSize(300, 0))
        self.full_menu_widget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.full_menu_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.full_menu_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.full_menu_widget.setLineWidth(0)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_8.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.logo_div = QtWidgets.QFrame(self.full_menu_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_div.sizePolicy().hasHeightForWidth())
        self.logo_div.setSizePolicy(sizePolicy)
        self.logo_div.setMinimumSize(QtCore.QSize(300, 80))
        self.logo_div.setMaximumSize(QtCore.QSize(500, 16777215))
        self.logo_div.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_div.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_div.setObjectName("logo_div")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.logo_div)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_icon_2 = QtWidgets.QPushButton(self.logo_div)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_icon_2.sizePolicy().hasHeightForWidth())
        self.logo_icon_2.setSizePolicy(sizePolicy)
        self.logo_icon_2.setMinimumSize(QtCore.QSize(120, 80))
        self.logo_icon_2.setMaximumSize(QtCore.QSize(120, 80))
        self.logo_icon_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/svg_icon/logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo_icon_2.setIcon(icon2)
        self.logo_icon_2.setIconSize(QtCore.QSize(80, 80))
        self.logo_icon_2.setObjectName("logo_icon_2")
        self.horizontalLayout_3.addWidget(self.logo_icon_2)
        self.logo_title = QtWidgets.QLabel(self.logo_div)
        self.logo_title.setObjectName("logo_title")
        self.horizontalLayout_3.addWidget(self.logo_title)
        self.verticalLayout_8.addWidget(self.logo_div, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.test_lessons_div_2 = QtWidgets.QVBoxLayout()
        self.test_lessons_div_2.setContentsMargins(25, -1, -1, -1)
        self.test_lessons_div_2.setSpacing(0)
        self.test_lessons_div_2.setObjectName("test_lessons_div_2")
        self.test_lessons_div_2__text_button = QtWidgets.QPushButton(self.full_menu_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_lessons_div_2__text_button.sizePolicy().hasHeightForWidth())
        self.test_lessons_div_2__text_button.setSizePolicy(sizePolicy)
        self.test_lessons_div_2__text_button.setMinimumSize(QtCore.QSize(25, 50))
        self.test_lessons_div_2__text_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/svg_icon/test.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("images/svg_icon/tets_white.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.test_lessons_div_2__text_button.setIcon(icon3)
        self.test_lessons_div_2__text_button.setIconSize(QtCore.QSize(50, 50))
        self.test_lessons_div_2__text_button.setCheckable(True)
        self.test_lessons_div_2__text_button.setAutoExclusive(True)
        self.test_lessons_div_2__text_button.setObjectName("test_lessons_div_2__text_button")
        self.test_lessons_div_2.addWidget(self.test_lessons_div_2__text_button, 0, QtCore.Qt.AlignLeft)
        self.test_lessons_div_2__lessons_button = QtWidgets.QPushButton(self.full_menu_widget)
        self.test_lessons_div_2__lessons_button.setMinimumSize(QtCore.QSize(25, 50))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/svg_icon/lessons.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("images/svg_icon/lessons_white.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("images/svg_icon/lessons_white.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.test_lessons_div_2__lessons_button.setIcon(icon4)
        self.test_lessons_div_2__lessons_button.setIconSize(QtCore.QSize(50, 50))
        self.test_lessons_div_2__lessons_button.setCheckable(True)
        self.test_lessons_div_2__lessons_button.setAutoExclusive(True)
        self.test_lessons_div_2__lessons_button.setObjectName("test_lessons_div_2__lessons_button")
        self.test_lessons_div_2.addWidget(self.test_lessons_div_2__lessons_button, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_8.addLayout(self.test_lessons_div_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 110, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.color_setting_div_2 = QtWidgets.QFrame(self.full_menu_widget)
        self.color_setting_div_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_setting_div_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_setting_div_2.setObjectName("color_setting_div_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.color_setting_div_2)
        self.verticalLayout_2.setContentsMargins(25, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.color_setting_div_2__color_button = QtWidgets.QPushButton(self.color_setting_div_2)
        self.color_setting_div_2__color_button.setMinimumSize(QtCore.QSize(0, 50))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/svg_icon/palette.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("images/svg_icon/palette_white.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.color_setting_div_2__color_button.setIcon(icon5)
        self.color_setting_div_2__color_button.setIconSize(QtCore.QSize(50, 50))
        self.color_setting_div_2__color_button.setCheckable(True)
        self.color_setting_div_2__color_button.setAutoExclusive(True)
        self.color_setting_div_2__color_button.setObjectName("color_setting_div_2__color_button")
        self.verticalLayout_2.addWidget(self.color_setting_div_2__color_button, 0, QtCore.Qt.AlignLeft)
        self.color_setting_div_2__setting_button = QtWidgets.QPushButton(self.color_setting_div_2)
        self.color_setting_div_2__setting_button.setMinimumSize(QtCore.QSize(0, 50))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/svg_icon/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("images/svg_icon/settings_white.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.color_setting_div_2__setting_button.setIcon(icon6)
        self.color_setting_div_2__setting_button.setIconSize(QtCore.QSize(50, 50))
        self.color_setting_div_2__setting_button.setCheckable(True)
        self.color_setting_div_2__setting_button.setAutoExclusive(True)
        self.color_setting_div_2__setting_button.setObjectName("color_setting_div_2__setting_button")
        self.verticalLayout_2.addWidget(self.color_setting_div_2__setting_button, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_8.addWidget(self.color_setting_div_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.about_profile_div_2 = QtWidgets.QVBoxLayout()
        self.about_profile_div_2.setContentsMargins(25, -1, -1, -1)
        self.about_profile_div_2.setSpacing(0)
        self.about_profile_div_2.setObjectName("about_profile_div_2")
        self.about_profile_div_2__about_button = QtWidgets.QPushButton(self.full_menu_widget)
        self.about_profile_div_2__about_button.setMinimumSize(QtCore.QSize(0, 50))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/svg_icon/about.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("images/svg_icon/about_white.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.about_profile_div_2__about_button.setIcon(icon7)
        self.about_profile_div_2__about_button.setIconSize(QtCore.QSize(50, 50))
        self.about_profile_div_2__about_button.setCheckable(True)
        self.about_profile_div_2__about_button.setAutoExclusive(True)
        self.about_profile_div_2__about_button.setObjectName("about_profile_div_2__about_button")
        self.about_profile_div_2.addWidget(self.about_profile_div_2__about_button, 0, QtCore.Qt.AlignLeft)
        self.about_profile_div_2__profile_button = QtWidgets.QPushButton(self.full_menu_widget)
        self.about_profile_div_2__profile_button.setMinimumSize(QtCore.QSize(0, 50))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/svg_icon/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap("images/svg_icon/user_white.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.about_profile_div_2__profile_button.setIcon(icon8)
        self.about_profile_div_2__profile_button.setIconSize(QtCore.QSize(50, 50))
        self.about_profile_div_2__profile_button.setCheckable(True)
        self.about_profile_div_2__profile_button.setAutoExclusive(True)
        self.about_profile_div_2__profile_button.setObjectName("about_profile_div_2__profile_button")
        self.about_profile_div_2.addWidget(self.about_profile_div_2__profile_button, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_8.addLayout(self.about_profile_div_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 2, 1)
        self.icon_menu_widget = QtWidgets.QFrame(self.centralwidget)
        self.icon_menu_widget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.icon_menu_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.icon_menu_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.icon_menu_widget.setObjectName("icon_menu_widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.icon_menu_widget)
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.logo_icon_1 = QtWidgets.QPushButton(self.icon_menu_widget)
        self.logo_icon_1.setMinimumSize(QtCore.QSize(80, 80))
        self.logo_icon_1.setMaximumSize(QtCore.QSize(80, 80))
        self.logo_icon_1.setText("")
        self.logo_icon_1.setIcon(icon2)
        self.logo_icon_1.setIconSize(QtCore.QSize(80, 80))
        self.logo_icon_1.setObjectName("logo_icon_1")
        self.verticalLayout_7.addWidget(self.logo_icon_1, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.test_lessons_div_1 = QtWidgets.QVBoxLayout()
        self.test_lessons_div_1.setSpacing(0)
        self.test_lessons_div_1.setObjectName("test_lessons_div_1")
        self.test_lessons_div_1__text_button = QtWidgets.QPushButton(self.icon_menu_widget)
        self.test_lessons_div_1__text_button.setMinimumSize(QtCore.QSize(50, 50))
        self.test_lessons_div_1__text_button.setMaximumSize(QtCore.QSize(240, 240))
        self.test_lessons_div_1__text_button.setStyleSheet("")
        self.test_lessons_div_1__text_button.setText("")
        self.test_lessons_div_1__text_button.setIcon(icon3)
        self.test_lessons_div_1__text_button.setIconSize(QtCore.QSize(50, 50))
        self.test_lessons_div_1__text_button.setCheckable(True)
        self.test_lessons_div_1__text_button.setAutoExclusive(True)
        self.test_lessons_div_1__text_button.setObjectName("test_lessons_div_1__text_button")
        self.test_lessons_div_1.addWidget(self.test_lessons_div_1__text_button, 0, QtCore.Qt.AlignHCenter)
        self.test_lessons_div_1__lessons_button = QtWidgets.QPushButton(self.icon_menu_widget)
        self.test_lessons_div_1__lessons_button.setMinimumSize(QtCore.QSize(50, 50))
        self.test_lessons_div_1__lessons_button.setMaximumSize(QtCore.QSize(240, 240))
        self.test_lessons_div_1__lessons_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/svg_icon/lessons.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap("images/svg_icon/lessons_white.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.test_lessons_div_1__lessons_button.setIcon(icon9)
        self.test_lessons_div_1__lessons_button.setIconSize(QtCore.QSize(50, 50))
        self.test_lessons_div_1__lessons_button.setCheckable(True)
        self.test_lessons_div_1__lessons_button.setAutoExclusive(True)
        self.test_lessons_div_1__lessons_button.setObjectName("test_lessons_div_1__lessons_button")
        self.test_lessons_div_1.addWidget(self.test_lessons_div_1__lessons_button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addLayout(self.test_lessons_div_1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 110, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.color_setting_div_1 = QtWidgets.QVBoxLayout()
        self.color_setting_div_1.setSpacing(0)
        self.color_setting_div_1.setObjectName("color_setting_div_1")
        self.color_setting_div_1__colors_button = QtWidgets.QPushButton(self.icon_menu_widget)
        self.color_setting_div_1__colors_button.setMinimumSize(QtCore.QSize(50, 50))
        self.color_setting_div_1__colors_button.setMaximumSize(QtCore.QSize(255, 255))
        self.color_setting_div_1__colors_button.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/svg_icon/palette.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap("images/svg_icon/palette_white.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap("images/svg_icon/palette_white.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap("images/svg_icon/palette_white.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.color_setting_div_1__colors_button.setIcon(icon10)
        self.color_setting_div_1__colors_button.setIconSize(QtCore.QSize(50, 50))
        self.color_setting_div_1__colors_button.setCheckable(True)
        self.color_setting_div_1__colors_button.setAutoExclusive(True)
        self.color_setting_div_1__colors_button.setObjectName("color_setting_div_1__colors_button")
        self.color_setting_div_1.addWidget(self.color_setting_div_1__colors_button, 0, QtCore.Qt.AlignHCenter)
        self.color_setting_div_1__settings_button = QtWidgets.QPushButton(self.icon_menu_widget)
        self.color_setting_div_1__settings_button.setMinimumSize(QtCore.QSize(50, 50))
        self.color_setting_div_1__settings_button.setMaximumSize(QtCore.QSize(255, 255))
        self.color_setting_div_1__settings_button.setText("")
        self.color_setting_div_1__settings_button.setIcon(icon6)
        self.color_setting_div_1__settings_button.setIconSize(QtCore.QSize(50, 50))
        self.color_setting_div_1__settings_button.setCheckable(True)
        self.color_setting_div_1__settings_button.setAutoExclusive(True)
        self.color_setting_div_1__settings_button.setObjectName("color_setting_div_1__settings_button")
        self.color_setting_div_1.addWidget(self.color_setting_div_1__settings_button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addLayout(self.color_setting_div_1)
        spacerItem6 = QtWidgets.QSpacerItem(18, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem6)
        self.about_profile_div_1 = QtWidgets.QVBoxLayout()
        self.about_profile_div_1.setSpacing(0)
        self.about_profile_div_1.setObjectName("about_profile_div_1")
        self.about_profile_div_1__about_button = QtWidgets.QPushButton(self.icon_menu_widget)
        self.about_profile_div_1__about_button.setMinimumSize(QtCore.QSize(50, 50))
        self.about_profile_div_1__about_button.setMaximumSize(QtCore.QSize(255, 255))
        self.about_profile_div_1__about_button.setText("")
        self.about_profile_div_1__about_button.setIcon(icon7)
        self.about_profile_div_1__about_button.setIconSize(QtCore.QSize(50, 50))
        self.about_profile_div_1__about_button.setCheckable(True)
        self.about_profile_div_1__about_button.setAutoExclusive(True)
        self.about_profile_div_1__about_button.setAutoRepeatDelay(-6)
        self.about_profile_div_1__about_button.setObjectName("about_profile_div_1__about_button")
        self.about_profile_div_1.addWidget(self.about_profile_div_1__about_button, 0, QtCore.Qt.AlignHCenter)
        self.about_profile_div_1__profile_button = QtWidgets.QPushButton(self.icon_menu_widget)
        self.about_profile_div_1__profile_button.setMinimumSize(QtCore.QSize(50, 50))
        self.about_profile_div_1__profile_button.setMaximumSize(QtCore.QSize(255, 255))
        self.about_profile_div_1__profile_button.setText("")
        self.about_profile_div_1__profile_button.setIcon(icon8)
        self.about_profile_div_1__profile_button.setIconSize(QtCore.QSize(50, 50))
        self.about_profile_div_1__profile_button.setCheckable(True)
        self.about_profile_div_1__profile_button.setAutoExclusive(True)
        self.about_profile_div_1__profile_button.setObjectName("about_profile_div_1__profile_button")
        self.about_profile_div_1.addWidget(self.about_profile_div_1__profile_button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addLayout(self.about_profile_div_1)
        self.gridLayout.addWidget(self.icon_menu_widget, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        self.burger.toggled['bool'].connect(self.icon_menu_widget.setVisible)  # type: ignore
        self.burger.toggled['bool'].connect(self.full_menu_widget.setHidden)  # type: ignore
        self.test_lessons_div_1__text_button.toggled['bool'].connect(
            self.test_lessons_div_2__text_button.setChecked)  # type: ignore
        self.test_lessons_div_1__lessons_button.toggled['bool'].connect(
            self.test_lessons_div_2__lessons_button.setChecked)  # type: ignore
        self.color_setting_div_1__colors_button.toggled['bool'].connect(
            self.color_setting_div_2__color_button.setChecked)  # type: ignore
        self.about_profile_div_1__about_button.toggled['bool'].connect(
            self.about_profile_div_2__about_button.setChecked)  # type: ignore
        self.about_profile_div_1__profile_button.toggled['bool'].connect(
            self.about_profile_div_2__profile_button.setChecked)  # type: ignore
        self.test_lessons_div_2__text_button.toggled['bool'].connect(
            self.test_lessons_div_1__text_button.setChecked)  # type: ignore
        self.color_setting_div_2__color_button.toggled['bool'].connect(
            self.color_setting_div_1__colors_button.setChecked)  # type: ignore
        self.about_profile_div_2__about_button.toggled['bool'].connect(
            self.about_profile_div_1__about_button.setChecked)  # type: ignore
        self.about_profile_div_2__profile_button.toggled['bool'].connect(
            self.about_profile_div_1__profile_button.setChecked)  # type: ignore
        self.color_setting_div_2__setting_button.toggled['bool'].connect(
            self.color_setting_div_1__settings_button.setChecked)  # type: ignore
        self.color_setting_div_1__settings_button.toggled['bool'].connect(
            self.color_setting_div_2__setting_button.setChecked)  # type: ignore
        self.logo_icon_1.toggled['bool'].connect(self.logo_icon_2.setChecked)  # type: ignore
        self.logo_icon_2.toggled['bool'].connect(self.logo_icon_1.setChecked)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_window.setText(_translate("MainWindow", "ываыафыщаыфращ"))
        self.label.setText(_translate("MainWindow", "test"))
        self.label_2.setText(_translate("MainWindow", "lessons"))
        self.label_3.setText(_translate("MainWindow", "Colors"))
        self.label_4.setText(_translate("MainWindow", "Setting"))
        self.label_5.setText(_translate("MainWindow", "About"))
        self.label_6.setText(_translate("MainWindow", "Profile"))
        self.logo_title.setText(_translate("MainWindow", "blidingtype"))
        self.test_lessons_div_2__text_button.setText(_translate("MainWindow", "   test"))
        self.test_lessons_div_2__lessons_button.setText(_translate("MainWindow", "   lessons"))
        self.color_setting_div_2__color_button.setText(_translate("MainWindow", "   colors"))
        self.color_setting_div_2__setting_button.setText(_translate("MainWindow", "   settings"))
        self.about_profile_div_2__about_button.setText(_translate("MainWindow", "   about"))
        self.about_profile_div_2__profile_button.setText(_translate("MainWindow", "   profile"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())