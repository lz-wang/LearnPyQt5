# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/菜单和工具栏.html
# 例4 右键菜单


import sys
from PyQt5.QtWidgets import QMainWindow, QMenu, QApplication, qApp


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context Menu')
        self.show()

    def contextMenuEvent(self, event):
        cMenu = QMenu(self)

        newAct = cMenu.addAction('New')
        openAct = cMenu.addAction('Open')
        quitAct = cMenu.addAction('Quit')
        action = cMenu.exec_(self.mapToGlobal(event.pos()))  # 使用exec_()方法显示菜单
        # mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标

        if action == quitAct:
            qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
