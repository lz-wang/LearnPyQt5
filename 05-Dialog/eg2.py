#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/对话框.html
# 例2 选取颜色


import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QFrame,
                             QPushButton, QColorDialog)
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        color = QColor(0, 0, 0)

        self.btn = QPushButton('colorDlg', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.frame = QFrame(self)
        self.frame.setStyleSheet("QWidget {background-color: %s}" % color.name())
        self.frame.setGeometry(130, 25, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.frame.setStyleSheet("QWidget {background-color: %s}" % color.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
