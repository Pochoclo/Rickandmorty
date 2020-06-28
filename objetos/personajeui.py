__author__ = 'NicoS'


from PyQt4 import QtGui, QtCore
from objetos.sprite import Sprite
import time
import os
import constantes


class PersonaUI(QtGui.QLabel):
    JUGADORES = 0

    def __init__(self, parent, x, y, signal):
        super().__init__(parent)
        self.signal = signal
        self.signal.posicion_signal.connect(self.actualiza_posicion)
        self.signal.disparo_signal.connect(self.atacar)
        self.signal.sprite_signal.connect(self.actualiza_sprite)
        self.x = x
        self.y = y
        ancho = 125
        alto = 162
        frame = 4
        paso = 0.1
        self.setGeometry(x, y, 50, 70)
        self.imagen = constantes.PERSONAJES[PersonaUI.JUGADORES]
        self.sprite = Sprite(signal, ancho, alto, frame, paso)
        PersonaUI.JUGADORES += 1
        self.actualiza_sprite(0, 0)
        self.show()

    def actualiza_sprite(self, i, j, ancho=125, alto=162, invertido=False):
        if 'morty_fullart' in self.imagen:
            correccion = (4, 4, 636)
        else:
            correccion = (4, 4, 732)
        y = j * alto + correccion[2] + correccion[1] * (j + 1)
        x = i * ancho + correccion[0] * (i + 1)
        q = QtCore.QRect(x, y, ancho, alto)
        pixmap = QtGui.QPixmap(os.getcwd()+'/assets/sprites/'+self.imagen)
        pixmap = pixmap.copy(q)
        if invertido:
            pixmap = pixmap.transformed(QtGui.QTransform().scale(-1, 1))
        self.setScaledContents(True)
        self.setPixmap(pixmap)
        self.setScaledContents(True)
        self.show()

    def actualiza_posicion(self, x, y, direccion):
        self.x = x
        self.y = y
        self.setGeometry(self.x, self.y, 50, 50)
        if direccion == 'i':
            self.sprite.set_j(1)
            self.sprite.set_invertido(False)
        elif direccion == 'd':
            self.sprite.set_j(1)
            self.sprite.set_invertido(True)
        elif direccion == 'a':
            self.sprite.set_j(2)
            self.sprite.set_invertido(False)
        elif direccion == 'n':
            self.sprite.set_j(0)
        if not self.sprite.isRunning() and direccion != 'n':
            self.sprite.start()

    def atacar(self):
        self.actualiza_sprite(2, 2)