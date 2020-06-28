__author__ = 'NicoS'

from PyQt4 import QtCore


class PelotaSignal(QtCore.QObject):
    posicion_signal = QtCore.pyqtSignal(int, int)
    impacto_signal = QtCore.pyqtSignal()


class ObjetoSignal(QtCore.QObject):
    posicion_signal = QtCore.pyqtSignal(int, int, str)
    impacto_signal = QtCore.pyqtSignal()


class DisparoSignal(QtCore.QObject):
    posicion_signal = QtCore.pyqtSignal(int, int)
    sprite_signal = QtCore.pyqtSignal(int, int, int, int, bool)
    esconde_signal = QtCore.pyqtSignal()
    impacto_signal = QtCore.pyqtSignal(int, int, int)


class PersonajeSignal(QtCore.QObject):
    main_signal = QtCore.pyqtSignal()
    posicion_signal = QtCore.pyqtSignal(int, int, str)
    disparo_signal = QtCore.pyqtSignal(int, int)
    sprite_signal = QtCore.pyqtSignal(int, int, int, int, bool)
    vidas_signal = QtCore.pyqtSignal(int)


class MainSignal(QtCore.QObject):
    main_signal = QtCore.pyqtSignal(bool)

    pausar_juego = QtCore.pyqtSignal(bool)
    tiempo_signal = QtCore.pyqtSignal(int)

    jugadores_signal = QtCore.pyqtSignal(bool)
    ball_signal = QtCore.pyqtSignal(int, int, int, QtCore.QObject)
    human_signal = QtCore.pyqtSignal(int, int, QtCore.QObject)
    disparo_signal = QtCore.pyqtSignal(int, int, QtCore.QObject)
    objeto_signal = QtCore.pyqtSignal(int, int, QtCore.QObject, str)

    teclado_signal = QtCore.pyqtSignal(str)
    puntaje_signal = QtCore.pyqtSignal(int)


