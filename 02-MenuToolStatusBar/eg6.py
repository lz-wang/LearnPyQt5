# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/菜单和工具栏.html
# 例6 主窗口


import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 文字编辑区，可使用右键菜单
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        # 退出动作
        exitAct = QAction(QIcon('exit.png'), '&EXIT', self)
        exitAct.setShortcut('Ctrl+W')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(self.close)

        # 启用状态栏
        self.statusBar()

        # 设置菜单栏
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)  # for macOS only, to show menu in APP window
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAct)

        # 设置工具栏
        toolBar = self.addToolBar('Exit')
        toolBar.addAction(exitAct)

        # 设置窗口
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
