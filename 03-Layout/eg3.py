#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/布局管理.html
# 例3 栅格布局


import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QGridLayout)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建栅格布局
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Clear', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        # 创建栅格矩阵
        positions = [(i, j) for i in range(5) for j in range(4)]

        # 将对应元素依次放入对应的栅格之中
        for position, name in zip(positions, names):
            if name == '':
                continue
            else:
                btn = QPushButton(name)
                grid.addWidget(btn, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
