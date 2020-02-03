#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/事件和信号.html
# 例3 事件对象


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        self.label = QLabel('X = 0, Y = 0', self)
        grid.addWidget(self.label, 0, 0, Qt.AlignCenter)

        self.setMouseTracking(True)
        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    # 定义光标移动事件
    def mouseMoveEvent(self, e):
        x, y = e.x(), e.y()
        text = 'X = {0}, Y = {1}'.format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
