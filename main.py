__author__ = 'NicoS'

import signals
from PyQt4 import QtGui
from backend import Juego
from frontend import MainWindow, GameWidget
from signals import MainSignal
import sys


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    signal = MainSignal()
    f = MainWindow(signal)
    f.show()
    b = Juego(signal)
    app.exec_()