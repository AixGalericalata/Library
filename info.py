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

        con = sqlite3.connect('library.db')
        cur = con.cursor()

        result = cur.execute("""
        SELECT * FROM library
        WHERE id = ?
        """, (id,)).fetchone()

        self.name.setText(str(result[1]))
        self.year.setText(str(result[3]))

        author_result = cur.execute("""
        SELECT name FROM authors WHERE id = ?
        """, (result[2],)).fetchone()

        self.author.setText(str(author_result[0]))

        genre_result = cur.execute("""
        SELECT name FROM genres WHERE id = ?
        """, (result[4],)).fetchone()

        self.genre.setText(str(genre_result[0]))
        pixmap = QPixmap(f'images/{result[5]}')
        if pixmap.isNull():
            pixmap = QPixmap('images/None.png')
        pixmap = pixmap.scaled(self.picture.size(), QtCore.Qt.KeepAspectRatio,
                               transformMode=QtCore.Qt.SmoothTransformation)
        self.picture.setAlignment(QtCore.Qt.AlignCenter)
        self.picture.setPixmap(pixmap)
