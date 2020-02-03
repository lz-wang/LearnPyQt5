#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/事件和信号.html
# 例2 重构事件处理器


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Event handler')
        self.show()

    # 事件响应：当按下Esc或者0按键时，关闭窗口
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape or Qt.Key_0:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

