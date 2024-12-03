from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from PyQt6.QtCore import Qt

from os import urandom
from data import HexData

class HexEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QtGui.QFont("Courier", 12))
        self.charw = self.fontMetrics().horizontalAdvance("9")
        self.charh = self.fontMetrics().height()
        self.adrw = self.charw * 8 + self.charw
        self.hexw = (16 * 3 + 1) * self.charw
        self.asciiw = (16 + 2) * self.charw
        self.asciipos = self.adrw + self.hexw
        self.sumw = self.asciipos + self.asciiw
        self.setMinimumSize(self.sumw, 1000)

        self.data = HexData()
        self.data.setData(bytearray(urandom(264)))

    def paintEvent(self, e):
        self.firstind = (e.rect().top() // self.charh - self.charh) * 16
        self.lastind = (e.rect().bottom() // self.charh + self.charh) * 16
        if self.firstind < 0: self.firstind = 0
        if self.lastind > len(self.data): self.lastind = len(self.data)
        qp = QPainter(self)
        self.paintBorders(qp, e)
        self.paintAddressArea(qp, e)
        self.paintHexArea(qp, e)
        self.paintTextArea(qp, e)

    def mousePressEvent(self, e):
        if not e.button() == Qt.MouseButton.LeftButton:
            return
        xpos = e.pos().x()
        ypos = e.pos().y()
        if xpos < self.adrw or xpos > self.asciipos:
            return
        ind = self.pointToHexIndex(e.pos())
        if ind > len(self.data) * 2 - 1:
            return
        print("ind")

    def pointToHexIndex(self, pos):
        if pos.x() > self.adrw and pos.x() < self.asciipos - self.charw:
            x = (pos.x() - self.adrw) // self.charw
            if x % 3 == 2:
                x = (x // 3) * 2 + 1
            else:
                x = (x // 3) * 2
            y = (pos.y() // self.charh) * 16 * 2
        else:
            return -1
        return x + y

    def paintBorders(self, qp, e):
        top, h = e.rect().top(), self.height()
        qp.setPen(QPen(QColor(233, 231, 227), 2))
        qp.setBrush(QBrush(QColor(233, 231, 227)))
        qp.drawRect(0, top, self.adrw, h)
        qp.drawRect(self.asciipos, top, self.asciiw, h)
        qp.setPen(QPen(QColor(130, 135, 144), 1))
        qp.setBrush(QBrush(QColor(0, 0, 0, 0)))
        qp.drawRect(0, top, self.sumw - 1, h - 1)
        qp.drawLine(self.adrw, top, self.adrw, h)
        qp.drawLine(self.asciipos, top, self.asciipos, h)

    def paintAddressArea(self, qp, e):
        qp.setPen(QPen(QColor(0, 0, 0), 1))
        xpos = int(self.charw / 2)
        ypos = self.charh
        line = self.firstind
        while line < self.lastind:
            adr = line
            qp.drawText(xpos, ypos, f"{adr:08x}")
            ypos += self.charh
            line += 16

    def paintHexArea(self, qp, e):
        ypos = self.charh
        line = self.firstind
        while line < self.lastind:
            xpos = self.adrw
            for i in range(line, line + 16):
                if i >= len(self.data):
                    break
                hex = self.data[i]
                qp.drawText(xpos, ypos, " ")
                xpos += self.charw
                qp.drawText(xpos, ypos, f"{hex:02x}")
                xpos += self.charw * 2
            ypos += self.charh
            line += 16

    def paintTextArea(self, qp, e):
        ypos = self.charh
        line = self.firstind
        while line < self.lastind:
            xpos = self.asciipos + self.charw
            for i in range(line, line + 16):
                if i >= len(self.data):
                    break
                char = self.data[i]
                char = chr(char)
                qp.drawText(xpos, ypos, char)
                xpos += self.charw
            ypos += self.charh
            line += 16