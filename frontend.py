__author__ = 'NicoS'

from PyQt4 import QtCore, QtGui
from objetos.pelotaui import Pelotaui
from objetos.personajeui import PersonaUI
from objetos.disparoui import ShotUI
from objetos.objetosui import ObjetoUI
from random import choice
import os
import sys
import constantes
import time
import threading


class MainWindow(QtGui.QMainWindow):

    def __init__(self, signal):
        super().__init__()
        self.signal = signal
        self.signal.main_signal.connect(self.pantalla_juego)
        self.setGeometry(200, 100, 800, 600)
        self.setWindowTitle('Rick and Morty - SHOW ME WHAT YOU GOT!')
        self.setWindowIcon(QtGui.QIcon(os.getcwd()+'/assets/head_1.png'))
        self.widget_inicio = WidgetInicio(self.signal, parent=self)
        self.widget_juego = GameWidget(self.signal, parent=self)
        self.widget_inicio.hide()
        self.widget_juego.hide()
        self.pantalla_inicio()
        self.show()

    def pantalla_inicio(self):
        self.setCentralWidget(self.widget_inicio)
        self.widget_inicio.show()

    def pantalla_juego(self, singleplayer):
        self.setCentralWidget(self.widget_juego)
        self.widget_juego.setFocus(QtCore.Qt.ActiveWindowFocusReason)
        self.widget_juego.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.widget_juego.singleplayer = singleplayer
        self.widget_juego.crea_barra_juego()
        self.widget_juego.show()


class WidgetInicio(QtGui.QWidget):
    def __init__(self, signal, parent):
        super().__init__(parent)
        self.signal = signal
        self.setGeometry(0, 0, 800, 600)

        self.fondo = QtGui.QLabel(self)
        self.fondo.setGeometry(0, 0, 800, 600)
        p = QtGui.QPixmap(os.getcwd()+'/assets/wallpapers/'+'intro_wall.png')
        self.fondo.setPixmap(p)
        self.fondo.setScaledContents(True)
        self.fondo.show()

        self.t_cabeza = HeadUI(self)
        self.fondo_1 = QtGui.QLabel(self)
        self.fondo_1.setGeometry(0, 0, 800, 600)
        p = QtGui.QPixmap(os.getcwd()+'/assets/wallpapers/'+'intro_wall_1.png')
        self.fondo_1.setPixmap(p)
        self.fondo_1.setScaledContents(True)
        self.fondo_1.hide()

        self.rick = crea_label_cortado(self, 330, 350, 100, 250, 4, 2, 360, 730, 'sprites/rick_fullart')
        self.rick.hide()

        self.morty = crea_label_cortado(self, 20, 420, 80, 200, 4, 2, 230, 634, 'sprites/morty_fullart', invertido=True)
        self.morty.hide()

        font = QtGui.QFont('Terminal', 20)
        font.setBold(True)

        self.boton_1 = HoverButton(self)
        self.boton_1.setGeometry(110, 460, 180, 40)
        self.boton_1.setText('1 Player')
        self.boton_1.setFont(font)
        self.boton_2 = HoverButton(self)
        self.boton_2.setGeometry(110, 510, 180, 40)
        self.boton_2.setText('2 Players')
        self.boton_2.setFont(font)

        self.boton_1.clicked.connect(lambda: self.selecciona_players(True))
        self.boton_1.mousehover.connect(self.mouse_hover1)
        self.boton_2.clicked.connect(lambda: self.selecciona_players(False))
        self.boton_2.mousehover.connect(self.mouse_hover2)

        obj = QtGui.QSound(os.getcwd()+'/audios/Show_me_what_you_got.wav')
        obj.play()

    def mouse_hover1(self, enter):
        if enter:
            self.morty.show()
            self.rick.hide()
        else:
            self.morty.hide()
            self.rick.hide()

    def mouse_hover2(self, enter):
        if enter:
            self.morty.show()
            self.rick.show()
        else:
            self.morty.hide()
            self.rick.hide()

    def selecciona_players(self, singleplayer):
        if singleplayer:
            obj = QtGui.QSound(os.getcwd()+'/audios/oh_man.wav')
            obj.play()
        else:
            obj1 = QtGui.QSound(os.getcwd()+'/audios/mix.wav')
            obj1.play()
        self.signal.jugadores_signal.emit(singleplayer)
        self.hide()


class BarraJuego(QtGui.QWidget):
    def __init__(self, parent, signal, singleplayer):
        super().__init__(parent)
        self.signal = signal
        self.signal.pausar_juego.connect(self.pausar_timer)
        self.signal.tiempo_signal.connect(self.inicia_timer)
        self.singleplayer = singleplayer

        self.stage_time_label = Reloj(self)
        self.stage_time_label.setGeometry(350, 510, 130, 100)
        font = QtGui.QFont('Terminal', 20)
        font.setBold(True)
        self.timer = QtCore.QTimer()
        self.stage_time_label.connect(self.timer, QtCore.SIGNAL('timeout()'),
                                      self.stage_time_label, QtCore.SLOT('cuenta()'))

        self.stage_time_label.setText('Stage 1\n\n00:00')
        self.stage_time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stage_time_label.setFont(font)
        self.stage_time_label.setStyleSheet('color:white')
        self.stage_time_label.show()

        self.p1_face = crea_label_cortado(self, 20, 520, 71, 71, 4, 2, 230, 254,
                                          'sprites/morty_fullart', invertido=True)
        self.p1_face.show()

        self.boton_pausa = QtGui.QPushButton(self)
        self.boton_pausa.setGeometry(200, 540, 100, 40)
        self.boton_pausa.setText('Pausa')
        self.boton_pausa.clicked.connect(parent.pausar_juego)
        self.boton_pausa.show()

        self.boton_salir = QtGui.QPushButton(self)
        self.boton_salir.setGeometry(520, 540, 100, 40)
        self.boton_salir.setText('Salir')
        self.boton_salir.clicked.connect(parent.salir_juego)
        self.boton_salir.show()

        self.p1_name = QtGui.QLabel(self)
        self.p1_name.setGeometry(91, 520, 100, 35)
        self.p1_name.setText('Morty')
        f = QtGui.QFont('Segoe Script', 15)
        self.p1_name.setFont(f)
        self.p1_name.setStyleSheet('color: white')

        self.p1_lifes = QtGui.QLabel(self)
        self.p1_lifes.setGeometry(91, 555, 100, 35)
        self.p1_lifes.setText('x 2')
        self.p1_lifes.setFont(font)
        self.p1_lifes.setStyleSheet('color: white')
        if not singleplayer:
            self.p2_face = crea_label_cortado(self, 700, 520, 71, 71, 4, 2, 360, 413, 'sprites/rick_fullart')
            self.p2_face.show()
            self.p2_name = QtGui.QLabel(self)
            self.p2_name.setGeometry(650, 520, 100, 35)
            self.p2_name.setText('Rick')
            f = QtGui.QFont('Segoe Script', 15)
            self.p2_name.setFont(f)
            self.p2_name.setStyleSheet('color: white')

            self.p2_lifes = QtGui.QLabel(self)
            self.p2_lifes.setGeometry(650, 555, 100, 35)
            self.p2_lifes.setText('x 2')
            self.p2_lifes.setFont(font)
            self.p2_lifes.setStyleSheet('color: white')

    def inicia_timer(self, tiempo):
        self.stage_time_label.set_tiempo(tiempo)
        self.timer.start(1000)

    def pausar_timer(self):
        self.stage_time_label.pausar_tiempo()


class Reloj(QtGui.QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.tiempo = 200
        self.pausado = False

    def set_tiempo(self, tiempo):
        self.tiempo = tiempo

    def pausar_tiempo(self):
        if self.pausado:
            self.pausado = False
        else:
            self.pausado = True

    @QtCore.pyqtSlot()
    def cuenta(self):
        minutos = self.tiempo//60
        segundos = self.tiempo - minutos*60
        tiempo = [str(minutos).zfill(2), str(segundos).zfill(2)]
        self.setText('Stage 1\n\n{0}:{1}'.format(tiempo[0], tiempo[1]))
        if not self.pausado:
            self.tiempo -= 1


class GameWidget(QtGui.QWidget):

    def __init__(self, signal, singleplayer=True, parent=None):
        super().__init__(parent)
        self.setFocus()
        self.singleplayer = singleplayer
        self.signal = signal
        self.signal.human_signal.connect(self.crea_personaje)
        self.signal.ball_signal.connect(self.crea_pelota)
        self.signal.disparo_signal.connect(self.crea_disparo)
        self.setGeometry(0, 0, 800, 600)

        self.fondo = QtGui.QLabel(self)
        self.fondo.setGeometry(0, 0, 800, 500)
        self.estilo = choice(constantes.FONDOS)
        p = QtGui.QPixmap(os.getcwd()+'/assets/'+self.estilo[0])
        self.fondo.setPixmap(p)
        self.fondo.setScaledContents(True)
        self.fondo.show()
        self.crea_suelo()

        self.players = []
        self.pelotas = []
        self.disparos = []
        self.objetos = []
        self.show()
        self.juego_pausado = False

    def pausar_juego(self):
        self.signal.teclado_signal.emit('pause')
        if self.juego_pausado:
            self.juego_pausado = False
        else:
            self.juego_pausado = True

    def salir_juego(self):
        sys.exit()

    def crea_pelota(self, x, y, nivel, signal):
        p = Pelotaui(self, x, y, nivel, signal)
        p.show()
        self.pelotas.append(p)

    def crea_personaje(self, x, y, signal):
        p = PersonaUI(self, x, y, signal)
        p.show()
        self.players.append(p)

    def crea_disparo(self, x, y, signal):
        p = ShotUI(self, x, y, signal)
        p.show()
        self.disparos.append(p)

    def crea_objeto(self, x, y, tipo, signal):
        p = ObjetoUI(self, x, y, tipo, signal)
        p.show()
        self.objetos.append(p)

    def crea_suelo(self):
        # 25,15 -> 50x50 grassground
        # 25,75 -> 50x50 ground
        # el suelo inicia en 400
        for i in range(16):
            crea_label_cortado(self, i*50, constantes.ALTURA_BASE+50, 50, 50, 25, 15, 50, 50, self.estilo[1])
        for i in range(16):
            crea_label_cortado(self, i*50, constantes.ALTURA_BASE+100, 50, 50, 25, 75, 50, 50, self.estilo[1])

    def crea_barra_juego(self):
        self.barra = BarraJuego(self, self.signal, self.singleplayer)
        self.barra.setGeometry(0, 0, 800, 600)
        self.barra.show()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_G:
            self.salir_juego()
        elif QKeyEvent.key() == QtCore.Qt.Key_P:
            self.pausar_juego()
        if not self.juego_pausado:
            if self.singleplayer:
                if QKeyEvent.key() == QtCore.Qt.Key_Left:
                    self.signal.teclado_signal.emit('izquierda')
                    pass
                elif QKeyEvent.key() == QtCore.Qt.Key_Right:
                    self.signal.teclado_signal.emit('derecha')
                    pass
                elif QKeyEvent.key() == QtCore.Qt.Key_Space:
                    self.signal.teclado_signal.emit('arriba')
                    pass
            else:
                if QKeyEvent.key() == QtCore.Qt.Key_Left:
                    self.signal.teclado_signal.emit('izquierda')
                    pass
                elif QKeyEvent.key() == QtCore.Qt.Key_Right:
                    self.signal.teclado_signal.emit('derecha')
                    pass
                elif QKeyEvent.key() == QtCore.Qt.Key_Up:
                    self.signal.teclado_signal.emit('arriba')
                    pass
                elif QKeyEvent.key() == QtCore.Qt.Key_A:
                    self.signal.teclado_signal.emit('A')
                    pass
                elif QKeyEvent.key() == QtCore.Qt.Key_D:
                    self.signal.teclado_signal.emit('D')
                    pass
                elif QKeyEvent.key() == QtCore.Qt.Key_W:
                    self.signal.teclado_signal.emit('W')
                    pass

    def keyReleaseEvent(self, QKeyEvent):
        if self.singleplayer:
            if QKeyEvent.key() == QtCore.Qt.Key_Left:
                self.signal.teclado_signal.emit('p1')
                pass
            elif QKeyEvent.key() == QtCore.Qt.Key_Right:
                self.signal.teclado_signal.emit('p1')
                pass
        else:
            if QKeyEvent.key() == QtCore.Qt.Key_Left:
                self.signal.teclado_signal.emit('p1')
                pass
            elif QKeyEvent.key() == QtCore.Qt.Key_Right:
                self.signal.teclado_signal.emit('p1')
                pass
            elif QKeyEvent.key() == QtCore.Qt.Key_A:
                self.signal.teclado_signal.emit('p2')
                pass
            elif QKeyEvent.key() == QtCore.Qt.Key_D:
                self.signal.teclado_signal.emit('p2')
                pass


class HoverButton(QtGui.QPushButton):
    mousehover = QtCore.pyqtSignal(bool)

    def __init__(self, parent):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.setStyleSheet(
            'background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 0, 255),'
            ' stop:1 rgba(255, 85, 0, 255));'
            'border-radius: 25px;'
            'padding: 1px;'
            'color:white'
            )

    def enterEvent(self, *args, **kwargs):
        self.mousehover.emit(True)

    def leaveEvent(self, *args, **kwargs):
        self.mousehover.emit(False)


class HeadUI(QtCore.QThread):
    main_signal = QtCore.pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.main_signal.connect(self.start)

    def run(self):
        obj = QtGui.QSound(os.getcwd()+'/audios/Show_me_what_you_got.wav')
        obj.play()
        for i in range(6):
            self.parent.fondo_1.hide()
            time.sleep(0.1)
            self.parent.fondo_1.show()
            time.sleep(0.1)


def crea_label_cortado(parent, x, y, ancho, alto, i, j, ancho_sprite, alto_sprite, imagen, invertido=False):
    label = QtGui.QLabel(parent)
    label.setGeometry(x, y, ancho, alto)
    q = QtCore.QRect(i, j, ancho_sprite, alto_sprite)
    p = QtGui.QPixmap(os.getcwd()+'/assets/'+imagen+'.png')
    p = p.copy(q)
    if invertido:
        p = p.transformed(QtGui.QTransform().scale(-1, 1))
    label.setPixmap(p)
    label.setScaledContents(True)
    return label