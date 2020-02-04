#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/对话框.html
# 例1 输入文字


import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
                             QLineEdit, QInputDialog)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('textDlg', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 20)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
