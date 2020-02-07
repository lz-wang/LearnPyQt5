#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source: https://maicss.gitbooks.io/pyqt5/content/控件2.html
# 例9 下拉选项 QComboBox


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QComboBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        combo = QComboBox(self)
        combo.addItems(['macOS 10.15 Catalina',
                        'macOS 10.14 Mojave',
                        'macOS 10.13 High Sierra',
                        'macOS 10.12 Sierra',
                        'OS X 10.11 El Capitan',
                        'OS X 10.10 Yosemite',
                        'OS X 10.9 Mavericks',
                        'OS X 10.8 Mountain Lion',
                        'Mac OS X 10.7 Lion',
                        'Mac OS X 10.6 Snow Leopard',
                        'Mac OS X 10.5 Leopard',
                        'Mac OS X 10.4 Tiger',
                        'Mac OS X 10.3 Panther',
                        'Mac OS X 10.2 Jaguar',
                        'Mac OS X 10.1 Puma',
                        'Mac OS X 10.0 Cheetah'])
        combo.activated[str].connect(self.onActived)
        combo.move(50, 50)

        self.label = QLabel('macOS 10.15 Catalina', self)
        self.label.move(60, 150)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox (macOS version)')
        self.show()

    def onActived(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
