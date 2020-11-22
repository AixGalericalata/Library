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
        con = sqlite3.connect('library.db')
        self.cur = con.cursor()

    def initUI(self):
        uic.loadUi('main.ui', self)

        self.pushButton.clicked.connect(self.push)

    def push(self):
        request = self.lineEdit.text()
        if self.comboBox.currentText() == 'Автор':
            field = 'author'
        else:
            field = 'name'
        st = f'SELECT name FROM library WHERE {field} LIKE "%{request}%"'
        result = self.cur.execute(st).fetchall()

        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()
        #  self.tableWidget.itemSelectionChanged.connect(self.selected)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setColumnWidth(0, self.tableWidget.size().width())
        for i, elem in enumerate(result):
            item = QTableWidgetItem(elem[0])
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, 0, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())