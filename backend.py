__author__ = 'NicoS'

import threading
import signals
import time
import math
import constantes
import socket
from random import randint
from modelo.pelotas import Pelota, PelotaBoss, PelotaMentor, PelotaTpd
from modelo.personajes import Personaje
from modelo.disparo import Shot
from modelo.objetos import Objeto

IP = socket.gethostname()
PORT = 1232


class Juego(threading.Thread):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal
        self.daemon = True
        self.signal.jugadores_signal.connect(self.crear_personaje)
        self.signal.teclado_signal.connect(self.teclado_presionado)
        self.signal.pausar_juego.connect(self.pausar_juego)
        self.players = []
        self.pelotas = []
        self.disparos = []
        self.objetos = []
        self.juego_iniciado = False
        self.juego_pausado = False
        # self.collisions = CollisionHandler(self.players, self.pelotas)

    def teclado_presionado(self, comando):
        if comando == 'escape':
            pass
        elif comando == 'pause':
            self.pausar_juego()
        elif comando == 'izquierda' or comando == 'derecha' or comando == 'arriba':
            self.players[0].movimiento(comando)
            pass
        elif comando == 'p1':
            self.players[0].movimiento('detener')
            pass
        elif len(self.players) > 1:
            if comando == 'A':
                self.players[1].movimiento('izquierda')
                pass
            elif comando == 'D':
                self.players[1].movimiento('derecha')
                pass
            elif comando == 'W':
                self.players[1].movimiento('arriba')
                pass
            elif comando == 'p2':
                self.players[1].movimiento('detener')

    def movimiento(self, direccion):
        pass

    def pausar_juego(self):
        for objeto in self.players:
            objeto.pausa()
        for objeto in self.disparos:
            objeto.pausa()
        for objeto in self.pelotas:
            objeto.pausa()
        for objeto in self.objetos:
            objeto.pausa()

    def crear_personaje(self, singleplayer):
        p1x = 100
        p1y = constantes.ALTURA_BASE
        signal = signals.PersonajeSignal()
        signal.disparo_signal.connect(self.crear_disparo)
        p = Personaje(p1x, p1y, signal, self.pelotas)
        self.players.append(p)
        self.signal.human_signal.emit(p1x, p1y, signal)
        if not singleplayer:
            p2x = 400
            p2y = constantes.ALTURA_BASE
            signal = signals.PersonajeSignal()
            signal.disparo_signal.connect(self.crear_disparo)
            p = Personaje(p2x, p2y, signal, self.pelotas)
            self.players.append(p)
            self.signal.human_signal.emit(p2x, p2y, signal)
        self.signal.main_signal.emit(singleplayer)
        self.start()

    def crear_pelota(self, px=randint(0, 300), py=randint(0, 300), nivel=0, tipo=None):
        s = signals.PelotaSignal()
        # s.impacto_signal.connect(self.impacto_pelotas)
        p = None
        if not tipo:
            p = Pelota(px, py, s, nivel=nivel)
            self.pelotas.append(p)
            self.signal.ball_signal.emit(px, py, nivel, s)
        elif tipo == 'boss':
            p = PelotaBoss(nivel, px, py, s)
            self.pelotas.append(p)
            self.signal.ball_signal.emit(px, py, nivel, s)
        elif tipo == 'mentor':
            p = PelotaMentor(nivel, px, py, s)
            self.pelotas.append(p)
            self.signal.ball_signal.emit(px, py, nivel, s)
        elif tipo == 'python':
            pass
        return p

    def impacto_pelotas(self, x, y, nivel):
        nivel -= 1
        if nivel > 0:
            p = self.crear_pelota(px=x, py=y, nivel=nivel)
            p.start()
            p1 = self.crear_pelota(px=x, py=y, nivel=nivel)
            p1.cambiar_sentido()
            p1.start()

    def crear_disparo(self, x, y, tipo=None):
        s = signals.DisparoSignal()
        s.impacto_signal.connect(self.impacto_pelotas)
        if not tipo:
            p = Shot(s, x, y, self.pelotas)
            self.disparos.append(p)
            self.signal.disparo_signal.emit(x, y, s)
            p.start()

    def crear_objeto(self, tipo=None):
        s = signals.ObjetoSignal()
        x = randint(0, 800)
        y = randint(0, 200)
        p = Objeto(s, x, y, self.players)
        self.objetos.append(p)
        self.signal.objeto_signal.emit(x, y, s, '')
        p.start()

    def object_spawner(self):

        pass

    def run(self):
        tiempo_ejecucion = 0
        if not self.juego_iniciado:
            self.signal.tiempo_signal.emit(200)
            for player in self.players:
                player.start()
            for i in range(2):
                p = self.crear_pelota(nivel=2)
                if i % 2 == 0:
                    p.cambiar_sentido()
            for pelota in self.pelotas:
                pelota.start()
            self.juego_iniciado = True
        while not self.juego_pausado:
            time.sleep(0.01)
            tiempo_ejecucion += 0.01

    def etapa_1(self):
        # una nivel 2 -> mentor
        tiempo = 60
        self.pelotas = []
        p = signals.PelotaSignal()
        x = 100
        y = 100
        self.pelotas.append(PelotaMentor(2, x=x, y=y, signal=p))

    def etapa_2(self):
        # dos nivel 3 -> boss, boss
        self.pelotas = []
        for i in range(2):
            p = signals.PelotaSignal()
            x = 100 * (i + 1)
            y = 100
            self.pelotas.append(PelotaBoss(3, x=x, y=y, signal=p))

    def etapa_3(self):
        # una nivel 4, una nivel 2 -> boss(4), mentor
        pass

    def etapa_4(self):
        # una nivel 3, una python nivel 2 -> boss, python(2)
        pass

    def etapa_5(self):
        # una nivel 5 -> boss(5)
        pass

    def etapa_6(self):
        # dos python nivel 3 -> python(3), python(3)
        pass

    def etapa_7(self):
        # una nivel 2, pared, una nivel 5 -> mentor, pared, boss(5)
        pass

    def etapa_8(self):
        # dos nivel 2, pared, una nivel 3, pared, una python nivel 4 -> mentor, mentor, pared, boss, pared, python(4)
        pass


class Server(threading.Thread):

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((IP, PORT))
        self.socket.listen(5)

    def run(self):
        while True:
            pass
        pass


class Cliente(threading.Thread):

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self, ip):
        try:
            self.socket.connect((ip, PORT))
        except socket.error:
            print('Error Conectando con el servidor')
        else:
            self.start()

    def run(self):
        while True:
            pass


def distancia(a, b, r=5, correccion=50):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2) <= r