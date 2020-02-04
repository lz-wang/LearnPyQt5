#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/对话框.html
# 例4 选择文件


import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QAction,
                             QTextEdit, QFileDialog)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.jpg'), 'open', self)
        openFile.setShortcut('Ctrl + O')
        openFile.setStatusTip('open new file')
        openFile.triggered.connect(self.showDialog)

        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.resize(800, 600)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'open file', './')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
