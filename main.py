from sys import argv, exit
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton 
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor, QPen
from random import randint

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.paint)
        self.paintstate = False

    def paint(self):
        self.paintstate = True
        self.repaint()

    def paintEvent(self, event):
        if self.paintstate:
            qp = QPainter()
            qp.begin(self)
            self.getcircles(qp)
            qp.end()

    def getcircles(self, qp):
        qp.setPen(QPen(QColor(255, 255, 102), 5))
        qp.drawEllipse(randint(0, 600), randint(0, 400), randint(0, 200), randint(0, 200))

def main():
    app = QApplication(argv)
    window = App()
    window.show()
    exit(app.exec())

if __name__ == "__main__":
    main()
