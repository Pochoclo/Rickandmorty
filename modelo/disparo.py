__author__ = 'NicoS'

import threading
import time
import constantes
import math


class Shot(threading.Thread):
    def __init__(self, signal, x, y, pelotas):
        super().__init__()
        self.signal = signal
        self.pelotas = pelotas
        self.daemon = True
        self.x = x
        self.y = y
        self.velocidad = constantes.VELOCIDAD_DISPARO
        self.radio = constantes.RADIO_DISPARO
        self.impactado = False
        self.juego_pausado = False

    def pausa(self):
        if self.juego_pausado:
            self.juego_pausado = False
        else:
            self.juego_pausado = True

    def impacto(self):

        pass

    def distancia(self, a, b, r=5, correccion=50):
        return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2) <= a.radio + b.radio

    def actualiza_posicion(self):
        self.y += - self.velocidad
        impacto = list(filter(lambda x: self.distancia(self, x, self.radio) and not x.impactada, self.pelotas))
        if impacto:
            self.pausa()
            impacto[0].pelota_impactada()
            self.signal.impacto_signal.emit(impacto[0].x, impacto[0].y, impacto[0].nivel)
        self.signal.posicion_signal.emit(self.x, self.y)
        pass

    def run(self):
        while not self.impactado and self.y > 0:
            if not self.juego_pausado:
                self.actualiza_posicion()
            time.sleep(constantes.TIEMPO_SLEEP)
        self.signal.esconde_signal.emit()