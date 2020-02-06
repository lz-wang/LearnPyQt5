#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/控件1.html
# 例5 日历 QCalendarWidget


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QCalendarWidget, QVBoxLayout
from PyQt5.QtCore import QDate


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        vbox = QVBoxLayout(self)
        vbox.addWidget(cal)

        self.label = QLabel(self)
        date = cal.selectedDate()
        self.label.setText(date.toString())

        vbox.addWidget(self.label)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.label.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
