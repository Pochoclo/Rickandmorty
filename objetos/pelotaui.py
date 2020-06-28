__author__ = 'NicoS'

import os
import constantes as cte
from PyQt4 import QtCore, QtGui
from random import choice
import constantes


class Pelotaui(QtGui.QLabel):
    def __init__(self, parent, x, y, nivel, pelota_signal):
        super().__init__(parent)
        self.signal = pelota_signal
        self.signal.posicion_signal.connect(self.actualiza_posicion)
        self.signal.impacto_signal.connect(self.esconde)
        self.x = x
        self.y = y
        self.nivel = nivel
        self.radio = 0
        self.correccion = 0
        pixmap = QtGui.QPixmap(self.elige_imagen())
        self.setGeometry(x, y, self.radio, self.radio)

        self.show()
        self.setPixmap(pixmap)
        self.setScaledContents(True)
        # self.setFixedSize(pixmap.size())
        self.show()

    def elige_imagen(self):
        if self.nivel >= 3:
            self.radio = 150
            self.correccion = 75
            return os.getcwd()+'/assets/bubbles/'+choice(cte.COLOR_PELOTA)+'_boss.png'
        elif self.nivel == 2:
            self.radio = 100
            self.correccion = 50
            return os.getcwd()+'/assets/bubbles/'+choice(cte.COLOR_PELOTA)+'_mentor.png'
        else:
            self.radio = 50
            self.correccion = 25
            return os.getcwd()+'/assets/bubbles/'+choice(cte.COLOR_PELOTA)+'_tpd.png'

    def esconde(self):
        self.hide()

    def actualiza_posicion(self, x, y):
        self.x = x - self.correccion
        self.y = y - self.correccion
        self.setGeometry(self.x, self.y, self.radio, self.radio)
