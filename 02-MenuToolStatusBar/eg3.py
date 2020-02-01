# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/菜单和工具栏.html
# 例3 可勾选的菜单栏


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.status_bar = self.statusBar()
        self.initUI()

    def initUI(self):
        self.status_bar.showMessage('Ready')

        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)  # for macOS only, to show menu in APP window
        viewMenu = menuBar.addMenu('View')

        viewStatAct = QAction('View status bar', self, checkable=True)
        viewStatAct.setStatusTip('View status bar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check Menu')
        self.show()

    def toggleMenu(self, state):
        if state:
            self.status_bar.show()
        else:
            self.status_bar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
