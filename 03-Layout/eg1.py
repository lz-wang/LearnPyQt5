#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/布局管理.html
# 例1 绝对定位

"""
绝对定位：即利用像素信息对窗口元素进行定位
局限性：
    1、元素不会随着我们更改窗口的位置和大小而变化
    2、不能适用于不同的平台和不同分辨率的显示器
    3、更改应用字体大小会破坏布局
    4、如果我们决定重构这个应用，需要全部计算一下每个元素的位置和大小
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label_1 = QLabel('Python 3', self)
        label_1.move(15, 10)  # 将元素移动到对应的坐标位置，原点位置在窗口的左上角

        label_2 = QLabel('Qt 5', self)
        label_2.move(35, 40)

        label_3 = QLabel('PyQt 5', self)
        label_3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute Position')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
