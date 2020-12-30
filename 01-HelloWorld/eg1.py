#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/hello_world.html
# 例1 简单的窗口


import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)  # 重置大小
    w.move(300, 300)  # 注意：原点在屏幕的左上角而不是中心
    w.setWindowTitle('Simple')  # 窗口标题设置
    w.show()

    sys.exit(app.exec_())
