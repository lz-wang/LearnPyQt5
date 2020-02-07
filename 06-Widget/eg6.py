#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/控件2.html
# 例6 图片控件 QPixmap


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('redrock.jpg')

        label = QLabel(self)
        label.setPixmap(pixmap)

        hbox.addWidget(label)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
