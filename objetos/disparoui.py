__author__ = 'NicoS'

from PyQt4 import QtCore, QtGui
from objetos.sprite import Sprite
import os
import constantes


class ShotUI(QtGui.QLabel):
    def __init__(self, parent, x, y, disparo_signal):
        super().__init__(parent)
        self.signal = disparo_signal
        self.signal.posicion_signal.connect(self.actualiza_posicion)
        self.signal.sprite_signal.connect(self.actualiza_sprite)
        self.signal.esconde_signal.connect(self.esconde)
        self.signal.impacto_signal.connect(self.esconde)
        self.x = x
        self.y = y
        self.setGeometry(x, y, 64, 64)
        self.imagen = constantes.IMAGEN_DISPARO
        ancho = 64
        alto = 64
        frame = 4
        paso = 0.1
        self.correccion = constantes.CORRECCION_DISPARO
        self.sprite = Sprite(self.signal, ancho, alto, frame, paso)
        self.show()
        self.escondido = False

    def esconde(self):
        self.escondido = True
        self.hide()

    def actualiza_sprite(self, i, j, ancho=64, alto=64, invertido=False):
        y = j * alto
        x = i * ancho
        q = QtCore.QRect(x, y, ancho, alto)
        pixmap = QtGui.QPixmap(os.getcwd()+'/assets/sprites/'+self.imagen)
        pixmap = pixmap.copy(q)
        if invertido:
            pixmap = pixmap.transformed(QtGui.QTransform().scale(-1, 1))
        transform = QtGui.QTransform().rotate(90)
        pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
        self.setPixmap(pixmap)
        self.setScaledContents(True)
        if self.escondido:
            self.hide()
        else:
            self.show()

    def actualiza_posicion(self, x, y):
        self.x = x
        self.y = y
        self.setGeometry(self.x - self.correccion, self.y - self.correccion, 64, 64)
        if not self.sprite.isRunning():
            self.sprite.start()