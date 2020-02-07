#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/控件2.html
# 例8 拖拽分割线改变子窗口大小控件 QSplitter


import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout,
                             QFrame, QSplitter, QStyleFactory)
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        # 添加横向分隔控件
        sp1 = QSplitter(Qt.Horizontal)
        sp1.addWidget(topleft)
        sp1.addWidget(topright)

        # 添加纵向分割控件
        sp2 = QSplitter(Qt.Vertical)
        sp2.addWidget(sp1)
        sp2.addWidget(bottom)

        hbox = QHBoxLayout(self)
        hbox.addWidget(sp2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
