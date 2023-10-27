import sys
from math import sin, pi, cos
from random import randint

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.initUI()
        self.x = -1
        self.y = -1
        self.shape = 0
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Координаты')

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        if event.button() == Qt.LeftButton:
            self.shape = 1
        elif event.button() == Qt.RightButton:
            self.shape = -1
        self.update()

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.shape = 2
            self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        r = randint(20, 100)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))

        if self.x > -1 and self.y > -1 and self.shape == -1:

            qp.setBrush(QColor(color))
            qp.drawRect(self.x - r, self.y - r, 2 * r, 2 * r)

        elif self.x > -1 and self.y > -1 and self.shape == 1:

            qp.setBrush(QColor(color))

            qp.drawEllipse(self.x - r, self.y - r, 2 * r, 2 * r)

        elif self.x > -1 and self.y > -1 and self.shape == 2:
            angle = 2 * pi / 3
            qp.setBrush(QColor(color))

            points = QPolygon([QPoint(self.x - int(r * sin(0 * angle)), self.y - int(r * cos(0 * angle))),
                               QPoint(self.x - int(r * sin(1 * angle)), self.y - int(r * cos(1 * angle))),
                               QPoint(self.x - int(r * sin(2 * angle)), self.y - int(r * cos(2 * angle)))])
            qp.drawPolygon(points)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
