#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/控件1.html
# 例2 切换按钮 QPushButton


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QPushButton
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.color = QColor(0, 0, 0)
        redBtn = QPushButton('Red', self)
        redBtn.setCheckable(True)  # 可以按下的按钮
        redBtn.move(10, 10)
        redBtn.clicked[bool].connect(self.setColor)

        greenBtn = QPushButton('Green', self)
        greenBtn.setCheckable(True)  # 可以按下的按钮
        greenBtn.move(10, 40)
        greenBtn.clicked[bool].connect(self.setColor)

        blueBtn = QPushButton('Blue', self)
        blueBtn.setCheckable(True)  # 可以按下的按钮
        blueBtn.move(10, 70)
        blueBtn.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.color.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.color.setRed(val)
        elif source.text() == "Green":
            self.color.setGreen(val)
        else:
            self.color.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.color.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
