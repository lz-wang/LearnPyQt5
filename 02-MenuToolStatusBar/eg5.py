# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/菜单和工具栏.html
# 例5 工具栏


import sys
from PyQt5.QtWidgets import QMainWindow, QMenu, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&EXIT', self)
        exitAct.setShortcut('Ctrl+W')
        exitAct.triggered.connect(qApp.quit)

        self.tool_bar = self.addToolBar('Exit')
        self.tool_bar.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
