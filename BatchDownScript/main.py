#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QTextEdit,
                             QGridLayout, QApplication, QLabel, QSlider,
                             QMessageBox)


class BatchDown(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.inputEdit = QLineEdit()
        self.outputEdit = QTextEdit()
        self.makeBtn = QPushButton('生成链接')
        self.makeBtn.clicked.connect(self.makeURL)
        self.copyBtn = QPushButton('复制链接')
        self.copyBtn.clicked.connect(self.copyURL)

        self.s_label = QLabel('      Bilibili 播放列表视频个数 N = ')
        self.n_edit = QLineEdit('10')
        self.n_slider = QSlider(Qt.Horizontal, self)
        self.n_slider.valueChanged[int].connect(self.changeValue)
        self.N = int(self.n_edit.text())

        grid = QGridLayout()  # 栅格布局将整个窗口划分为若干的行列
        grid.setSpacing(10)

        grid.addWidget(self.inputEdit, 1, 0, 1, 4)
        grid.addWidget(self.makeBtn, 1, 4)
        grid.addWidget(self.s_label, 2, 1)
        grid.addWidget(self.n_edit, 2, 2)
        grid.addWidget(self.n_slider, 2, 4)
        grid.addWidget(self.outputEdit, 3, 0, 5, 4)
        grid.addWidget(self.copyBtn, 4, 4)
        self.setLayout(grid)

        self.resize(600, 400)
        self.setWindowTitle('生成B站播放列表地址')
        self.show()

    def closeEvent(self, event):  # 如果点击窗口的X，则会弹出以下的提示框
        reply = QMessageBox.question(self, '信息', '确认退出程序？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def makeURL(self):
        self.N = int(self.n_edit.text())
        url = self.inputEdit.text()
        if url == '':
            self.outputEdit.setText('不合法的地址！')
        else:
            self.outputEdit.setText(self.generateList(url))

    def copyURL(self):
        self.clipboard = QApplication.clipboard()
        url = self.outputEdit.toPlainText()
        self.clipboard.setText(url)
        self.outputEdit.selectAll()

    def generateList(self, str_in):
        text = ''
        for ch in str_in:
            text += ch
            if ch == '?':
                break
            elif text == str_in:
                return '不合法的地址！'

        str_out = text
        for i in range(self.N - 1):
            str_out += ('\n' + text + 'p=' + str(i + 2))
        return str_out

    def changeValue(self, value):
        self.N = value + 1
        self.n_edit.setText(str(value + 1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    b_list_url = BatchDown()
    sys.exit(app.exec_())
