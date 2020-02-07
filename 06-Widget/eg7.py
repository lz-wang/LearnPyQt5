#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/控件2.html
# 例7 行编辑 QLineEdit


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.move(60, 40)

        lineEdit = QLineEdit(self)
        lineEdit.move(60, 100)
        lineEdit.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    # 将label和edit绑定，即时更新label的内容
    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
