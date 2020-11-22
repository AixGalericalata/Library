import sqlite3
import sys

from PyQt5 import uic
from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QLabel, QLineEdit, QWidget, QApplication, QTableWidget, QHeaderView, \
    QAbstractItemView
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initDB()

    def initDB(self):
        pass
        #  con = sqlite3.connect('')
        #  self.cur = con.cursor()

    def initUI(self):
        uic.loadUi('main.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())