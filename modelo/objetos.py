__author__ = 'NicoS'

import threading
import random
import constantes
import time


class Objeto(threading.Thread):
    def __init__(self, signal, x, y, personas=None):
        super().__init__()
        self.signal = signal
        self.x = x
        self.y = y
        self.personajes = personas
        self.velocidad = 0
        self.tiempo_restante = random.randint(3, 10)
        self.juego_pausado = False
        self.tomado = False

    def pausa(self):
        if self.juego_pausado:
            self.juego_pausado = False
        else:
            self.juego_pausado = True

    def run(self):
        while not self.tomado:
            if self.juego_pausado:
                pass
            time.sleep(constantes.TIEMPO_SLEEP)
        pass


class Moneda(threading.Thread):
    def __init__(self, signal, x, y):
        super().__init__()
        self.signal = signal
        self.x = x
        self.y = y
        self.velocidad = 0
        self.tiempo_restante = random.randint(3, 10)

    def run(self):
        pass


class Billete(threading.Thread):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal

    def run(self):
        pass


class Vida(threading.Thread):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal

    def run(self):
        pass


class Tiempo(threading.Thread):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal

    def run(self):
        pass


class Alambre(threading.Thread):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal

    def run(self):
        pass


class Doble(threading.Thread):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal

    def run(self):
        pass


class Escudo(threading.Thread):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal

    def run(self):
        pass