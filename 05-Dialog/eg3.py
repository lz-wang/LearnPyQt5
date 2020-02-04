#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/对话框.html
# 例3 选择字体


import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout,
                             QPushButton, QLabel, QSizePolicy, QFontDialog)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        btn = QPushButton('fontDlg', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.clicked.connect(self.showDialog)
        btn.move(20, 20)

        self.label = QLabel('Knowledge only matters', self)
        self.label.move(130, 20)

        vbox.addWidget(btn)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
