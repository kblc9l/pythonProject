import sys
import threading
import time
from math import sin, pi, cos
from random import randint

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.timer = None
        self.flag = False
        self.initUI()
        self.x = -1
        self.y = -1
        self.shape = 0
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Координаты')

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.isActive)
        self.timer.start()

    def isActive(self):
        self.count += 1
        if self.count == 5:
            self.timer.stop()
            print('таймер остановлен')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
