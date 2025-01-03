from PyQt6 import QtCore

class HexData:
    def __init__(self):
        self.data = None

    def __len__(self):
        if self.data:
            return self.data.size()
        return 0

    def __getitem__(self, index):
        return int.from_bytes(self.data[index], "little")

    def __setitem__(self, index, data):
        self.data.replace(index, 1, bytes([data]))

    def replaceWithValue(self, pos, size, value):
        values = bytearray([value & 0xFF] * size)
        self.data.replace(pos, size, QtCore.QByteArray(values))

    def insert(self, pos, data):
        self.data.insert(pos, data)

    def remove(self, pos, size):
        values = bytearray(size)
        self.data.replace(pos, size, QtCore.QByteArray(values))

    def setData(self, data):
        if isinstance(data, (bytearray, bytes)):
            self.data = QtCore.QByteArray(data)
        elif isinstance(data, (QtCore.QByteArray)):
            self.data = data
        else:
            raise ValueError("Invalid Data Format. Needs to be a bytearray, bytes or QByteArray.")

    def getData(self):
        return self.data.data()