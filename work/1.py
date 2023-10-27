import csv
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView


class OlympResult(QMainWindow):

    def __init__(self):
        super().__init__()
        self.res = []
        self.tableWidget = None
        self.initUI()
        self.expensive = []

    def initUI(self):
        try:

            self.schools = QtWidgets.QComboBox(self)
            self.schools.setGeometry(QtCore.QRect(20, 10, 91, 22))
            self.schools.setObjectName("schools")
            self.classes = QtWidgets.QComboBox(self)
            self.classes.setGeometry(QtCore.QRect(139, 10, 91, 22))
            self.classes.setObjectName("classes")
            self.resultButton = QtWidgets.QPushButton(self)
            self.resultButton.setGeometry(QtCore.QRect(270, 10, 150, 23))
            self.resultButton.setObjectName("resultButton")
            self.resultButton.setText("Узнать результат")
            with open('rez.csv', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                self.expensive = [['Фамилия', 'Результат']]
                sh, cl = set(), set()

                for i in list(reader)[1:]:
                    self.res.append(i)
                    info = i[2].split('-')
                    name = i[1].split()[3]
                    score = int(i[-1])
                    self.expensive.append([name, score])
                    sh.add(info[2])
                    cl.add(info[3])

                self.schools.insertItems(0, ['Все'] + list(sh))
                self.classes.insertItems(0, ['Все'] + list(cl))

            self.setGeometry(100, 100, 600, 600)
            self.tableWidget = QTableWidget(self)
            self.tableWidget.move(0, 50)

            self.tableWidget.setColumnCount(2)
            self.tableWidget.setColumnWidth(0, 150)
            self.tableWidget.setColumnWidth(1, 150)

            self.tableWidget.setHorizontalHeaderLabels(self.expensive[0])
            self.tableWidget.setRowCount(len(self.expensive) - 1)

            row = 0
            for e in sorted(self.expensive[1:], key=lambda x: (int(x[1]), x[0]), reverse=True):
                self.tableWidget.setItem(row, 0, QTableWidgetItem(e[0]))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(e[1])))

                row += 1

            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
            self.tableWidget.adjustSize()

            self.resultButton.clicked.connect(self.run)
        except Exception as er:
            print(er)

    def run(self):
        try:
            s, cl = self.schools.currentText(), self.classes.currentText()

            expensive2 = []
            self.tableWidget.clear()
            for i in list(self.res):
                info = i[2].split('-')
                name = i[1].split()[3]
                score = int(i[-1])
                if s == 'Все' and cl == 'Все':
                    expensive2.append([name, score])
                elif s == 'Все':
                    if int(cl) == int(info[3]):
                        expensive2.append([name, score])
                elif cl == 'Все':
                    if int(s) == int(info[2]):
                        expensive2.append([name, score])
                elif int(s) == int(info[2]) and int(cl) == int(info[3]):
                    expensive2.append([name, score])
            expensive2.sort(key=lambda x: (int(x[1]), x[0]), reverse=True)
            row = 0
            self.tableWidget.setRowCount(len(expensive2))
            for e in expensive2:
                self.tableWidget.setItem(row, 0, QTableWidgetItem(e[0]))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(e[1])))

                row += 1
            self.tableWidget.setHorizontalHeaderLabels(['Фамилия', 'Результат'])

        except Exception:
            pass


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = OlympResult()
        ex.show()
        sys.exit(app.exec_())
    except Exception as er:
        print(er)
