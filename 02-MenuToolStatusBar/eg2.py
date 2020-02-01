# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/菜单和工具栏.html
# 例2 菜单栏


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&EXIT', self)
        exitAct.setShortcut('Ctrl+W')
        exitAct.setStatusTip('Exit Application')  # 状态栏提示
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)  # for macOS only, to show menu in APP window
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple Menu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
