#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/拖拽.html
# 例1 简单的拖拽


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    # 启用拖拽操作
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):  # 设定接受的文本类型：纯文本
            e.accept()
        else:
            e.ignore()

    # 重构drop操作，接受鼠标释放事件的行为
    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        btn = Button('Button', self)
        btn.move(190, 65)

        self.setWindowTitle('Simple Drag and Drop')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
