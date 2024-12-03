from sys import argv, exit
from random import randint

from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

from editor import HexEditor

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle("hextest")
        self.setGeometry(0, 0, 600, 600)
        self.setupUi()
        self.center()

    def setupUi(self):
        widget = QWidget()
        layout = QVBoxLayout()
        self.hex = HexEditor()
        layout.addWidget(self.hex)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def center(self):
        qr = self.frameGeometry()
        qr.moveCenter(self.screen().availableGeometry().center())
        self.move(qr.topLeft())

def main():
    app = QApplication(argv)
    window = App()
    window.show()
    exit(app.exec())

if __name__ == "__main__":
    main()