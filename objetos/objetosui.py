__author__ = 'NicoS'

from PyQt4 import QtCore, QtGui
import constantes
import os


class ObjetoUI(QtGui.QLabel):
    def __init__(self, parent, x, y, tipo, signal):
        super().__init__(parent)
        self.signal = signal
        self.x = x
        self.y = y
        self.setGeometry(x, y, constantes.ANCHO_OBJETOS, constantes.ALTO_OBJETOS)
        self.imagen = os.getcwd()+'/assets/props/'+constantes.IMAGEN_OBJETOS[tipo]
        p = QtGui.QPixmap(self.imagen)
        self.setPixmap(p)
        self.setScaledContents(True)
        self.show()

    def actualiza_posicion(self, x, y):
        self.x = x
        self.y = y
        self.setGeometry(self.x, self.y, constantes.ANCHO_OBJETOS, constantes.ALTO_OBJETOS)