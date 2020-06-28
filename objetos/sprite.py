__author__ = 'NicoS'

from PyQt4 import QtCore
import time


class Sprite(QtCore.QThread):
    def __init__(self, signal, ancho, alto, frame, paso):
        super().__init__()
        self.signal = signal
        self.j = 0
        self.frame = frame
        self.ancho = ancho
        self.alto = alto
        self.paso = paso
        self.invertido = False

    def set_j(self, j):
        self.j = j

    def set_invertido(self, invertido):
        self.invertido = invertido

    def run(self):
        for i in range(self.frame):
            self.signal.sprite_signal.emit(i, self.j, self.ancho, self.alto, self.invertido)
            time.sleep(self.paso)
        self.signal.sprite_signal.emit(0, self.j, self.ancho, self.alto, self.invertido)