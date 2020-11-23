import sqlite3
import sys

from PyQt5 import uic
from PyQt5 import Qt, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QLineEdit, QWidget, QApplication, QTableWidget, QHeaderView, \
    QAbstractItemView
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Info(QWidget):
    def __init__(self, id):
        super().__init__()
        self.initUI(id)

    def initUI(self, id):

        uic.loadUi('details.ui', self)
