__author__ = 'NicoS'

import threading
import time
import constantes
import math


class Personaje(threading.Thread):
    def __init__(self, x, y, signal, pelotas=None, objetos=None):
        super().__init__()
        self.signal = signal
        self.daemon = True
        self.pelotas = pelotas
        self.objetos = objetos
        self.x = x
        self.y = y
        self.radio = 25
        self.correccion = self.radio/2
        self.velocidad = constantes.VELOCIDAD_JUGADOR
        self.vidas = constantes.VIDAS_INICIALES
        self.moverse = 0
        self.juego_pausado = False

    def movimiento(self, comando):
        if comando == 'izquierda':
            self.moverse = - self.velocidad
        elif comando == 'derecha':
            self.moverse = self.velocidad
        elif comando == 'detener':
            self.moverse = 0
        elif comando == 'arriba':
            self.disparar()

    def disparar(self):
        self.signal.disparo_signal.emit(self.x, self.y)
        self.signal.posicion_signal.emit(self.x, self.y, 'a')

    def detecta_colision(self):
        pelota = list(filter(lambda x: self.distancia(self, x), self.pelotas))

    def distancia(self, a, b, r=5, correccion=50):
        return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2) <= a.radio + b.radio

    def actualiza_posicion(self):
        if 0 < self.moverse + self.x < constantes.TAMANO_MAPA[0]-40:
            self.x += self.moverse
        direccion = ''
        if self.moverse < 0:
            direccion = 'i'
        elif self.moverse > 0:
            direccion = 'd'
        else:
            direccion = 'n'
        self.signal.posicion_signal.emit(self.x - self.correccion, self.y, direccion)

    def pausa(self):
        if self.juego_pausado:
            self.juego_pausado = False
        else:
            self.juego_pausado = True

    def run(self):
        while self.vidas > 0:
            if not self.juego_pausado:
                self.actualiza_posicion()
                time.sleep(constantes.TIEMPO_SLEEP)