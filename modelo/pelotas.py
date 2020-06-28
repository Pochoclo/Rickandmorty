__author__ = 'NicoS'

import threading
import math
import time
import random
import constantes


class Pelota(threading.Thread):
    def __init__(self, x=0, y=0, signal=None, nivel=0):
        super().__init__()
        self.signal = signal
        self.daemon = True
        self.nivel = nivel
        self._radio = 0
        self.altura = constantes.ALTURA_BURBUJAS
        self.frecuencia = constantes.FRECUENCIA_BURBUJAS
        self.velocidad = constantes.VELOCIDAD_BURBUJAS
        self.x = x
        self.y = y
        self.impactada = False
        self.juego_pausado = False

    @property
    def radio(self):
        if self.nivel >= 3:
            self._radio = 150
        elif self.nivel == 2:
            self._radio = 100
        else:
            self._radio = 50
        return self._radio

    def cambiar_sentido(self):
        self.velocidad *= -1

    def pelota_impactada(self):
        self.impactada = True
        self.signal.impacto_signal.emit()  # self.x, self.y, self.nivel)
        # print('signal emitida')
        pass

    def pausa(self):
        if self.juego_pausado:
            self.juego_pausado = False
        else:
            self.juego_pausado = True

    def run(self):
        try:
            tiempo = math.acos(-math.sqrt(((constantes.ALTURA_BASE-self.y)**2)/self.altura**2))/self.frecuencia
        except ValueError:
            tiempo = 0
        # tiempo = 0  # math.acos((self.y - constantes.ALTURA_BASE)/self.altura)/self.frecuencia
        while not self.impactada:
            if not self.juego_pausado:
                self.x += self.velocidad
                tiempo += constantes.TIEMPO_SLEEP
                if tiempo >= 2*math.pi:
                    tiempo = 0
                if (self.x > 750 and self.velocidad > 0) or (self.x < 50 and self.velocidad < 0):
                    self.velocidad *= -1
                self.y = -abs(math.cos(self.frecuencia*tiempo))*self.altura + constantes.ALTURA_BASE
                self.signal.posicion_signal.emit(self.x, self.y)
            time.sleep(constantes.TIEMPO_SLEEP)


class PelotaBoss(Pelota):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.radio = constantes.RADIO_BOSS
        self.altura = 400
        self.velocidad = 5


class PelotaMentor(Pelota):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.radio = constantes.RADIO_MENTOR
        self.altura = 300
        self.velocidad = 7


class PelotaTpd(Pelota):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.radio = constantes.RADIO_TPD
        self.altura = 200
        self.velocidad = 10